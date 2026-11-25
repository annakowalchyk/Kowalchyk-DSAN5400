# ----------------  EXACT MATCH  -----------------
comparisons = TsvIterator("data/annotated-index-test.tsv", ExactMatch)
save_results(comparisons, "results_ExactMatch.tsv")

# Load results to dataframe for evaluation
print("Exact Match Results:\n")
results = pd.read_csv("results_ExactMatch.tsv", sep="\t")
results["predicted"] = results["score"].astype(int)
print("Precision:", evaluate(results, "precision"))
print("Recall:", evaluate(results, "recall"))
print("F1:", evaluate(results, "f1"))


# ----------------  JACCARD  -----------------
threshold = 0.5
comparisons = TsvIterator("data/annotated-index-test.tsv", Jaccard)
save_results(comparisons, "results_Jaccard.tsv")

# Load results to dataframe for evaluation
results = pd.read_csv("results_Jaccard.tsv", sep="\t")
results["predicted"] = (results["score"] >= threshold).astype(int)
print("Jaccard Results:\n")
print("Precision:", evaluate(results, "precision"))
print("Recall:", evaluate(results, "recall"))
print("F1:", evaluate(results, "f1"))

check_threshold(Jaccard)

# Precision and recall at 0.70
threshold = 0.70
comparisons = TsvIterator("data/annotated-index-test.tsv", Jaccard)
save_results(comparisons, "results_Jaccard.tsv")

# Load results to dataframe for evaluation
results = pd.read_csv("results_Jaccard.tsv", sep="\t")
results["predicted"] = (results["score"] >= threshold).astype(int)
print("Jaccard Results:\n")
print("Precision:", evaluate(results, "precision"))
print("Recall:", evaluate(results, "recall"))
print("F1:", evaluate(results, "f1"))


# ----------------  Levenshtein Distance  -----------------
# Run on training to get correct threshold
check_threshold(LevenshteinScore)

# Best threshold = 0.67
threshold = 0.67
comparisons = TsvIterator("data/annotated-index-test.tsv", LevenshteinScore)
save_results(comparisons, "results_Levenshtein.tsv")

# Load results to dataframe for evaluation
results = pd.read_csv("results_Levenshtein.tsv", sep="\t")
results["predicted"] = (results["score"] >= threshold).astype(int)
print("Levenshtein Results:\n")
print("Precision:", evaluate(results, "precision"))
print("Recall:", evaluate(results, "recall"))
print("F1:", evaluate(results, "f1"))