from itertools import chain
from numpy import transpose, identity

# This is 12x4 matrix where each row represents all 4 reviewers' ratings for one store,
# and each column represents each reviewer's ratings for all 12 store locations.
ratings = [[2, 2, 3, 2],
        [1, 1, None, 1],
        [3, 3, 3, 3],
        [3, 3, 3, 3],
        [2, 2, 2, 2],
        [1, 2, 3, 4],
        [4, 4, 4, 4],
        [1, 1, 2, 1],
        [2, 2, 2, 2],
        [None, 5, 5, 5],
        [None, None, 1, 1],
        [None, None, 3, None]]

# Helper function to calculate the agreement table:
#   - each row i corresponds to a store
#   - each column k represents a possible rating (1, 2, 3, or 4, in this case)
#   - each table entry r_ik is the number of reviewers who gave store i rating k
def get_agreement_table(ratings, categories):
    agreement = []

    for store in ratings:
        category_counts = list(map(lambda category: store.count(category), categories))
        if sum(category_counts) > 1: # Ignore any stores with less than two ratings
            agreement.append(category_counts)

    return agreement

# Helper function that returns the weighted count of reviewers who gave store i a rating that at least partially matched category k
# (For categorical data this is just the number of reviewers who picked category k)
def get_weighted_rater_count(weights_k, agreement_i):
    weighted_count = 0
    for i in range(len(agreement_i)):
        weighted_count += weights_k[i] * agreement_i[i]
    return weighted_count

# STEPS 1 & 2: CLEANING THE DATA AND BUILDING THE AGREEMENT TABLE

# Get the set of all possible ratings our reviewer can give
rating_categories = set(chain(*ratings)) 
# Remove the placeholder value for missing ratings
rating_categories.remove(None) 
agreement_table = get_agreement_table(ratings, rating_categories)

# n is the number of stores (more generally, the number of items being rated)
n = len(agreement_table) 
# q is the number of possible rating categories
q = len(rating_categories) 

# get an array with r_i (the total number of reviewers who rated the ith store) for all stores
raters_per_store = list(map(lambda r_ik: sum(r_ik), agreement_table)) 
# rhat is the average number of reviewers who rated each store
rhat = sum(raters_per_store) / n 

# STEP 3: CHOOSING A WEIGHT FUNCTION

# categorical weights are just the identity matrix (1 if the category matches and 0 otherwise)
weights = identity(len(rating_categories)) 

# STEP 4: CALCULATING OBSERVED PERCENT AGREEMENT (p_a)
percent_agreement = 0
for i in range(n): # Find the percent agreement for every store
    percent_agreement_i = 0
    for k in range(q): # Find the percent agreement for every category for the ith store
        rhat_ik = get_weighted_rater_count(weights[k], agreement_table[i])
        ri = sum(agreement_table[i]) # Number of people who rated this store
        percent_agreement_i_k = (agreement_table[i][k] * (rhat_ik - 1)) / (rhat * (ri - 1))
        percent_agreement_i += percent_agreement_i_k
    
    percent_agreement += percent_agreement_i

pa_prime = percent_agreement / n # Find the average store-level percent agreement

total_rating_count = n * rhat
pa = (1 - 1/(total_rating_count)) * pa_prime + 1/total_rating_count

# STEP 5: CALCULATING EXPECTED PERCENT AGREEMENT (p_e)
category_averages = list(map(lambda category: sum(category) / n, transpose(agreement_table)))
classification_probabilities = list(map(lambda category_average: category_average / rhat, category_averages))

pe = 0
for k in range(q): # For every possible pair of rating categories
    for l in range(q):
        # Add the probability of those two categories being chosen at random, weighted by how closely they match
        pe += classification_probabilities[k] * classification_probabilities[l] * weights[k][l] 

# STEP 6: CALCULATE KRIPPENDORFF'S ALPHA
alpha = (pa - pe) / (1 - pe)
print(f"Krippendorff's alpha: {alpha}")