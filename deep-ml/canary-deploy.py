def analyze_canary_deployment(canary_results: list, baseline_results: list, accuracy_tolerance: float = 0.05, latency_tolerance: float = 0.10) -> dict:
    """
    Analyze canary deployment health metrics for model rollout decision.
    
    Args:
        canary_results: list of prediction results from canary (new) model
                       Each dict has 'latency_ms', 'prediction', 'ground_truth'
        baseline_results: list of prediction results from baseline (existing) model
                         Each dict has 'latency_ms', 'prediction', 'ground_truth'
        accuracy_tolerance: max acceptable relative accuracy degradation (0.05 = 5%)
        latency_tolerance: max acceptable relative latency increase (0.10 = 10%)
    
    Returns:
        dict with canary/baseline metrics and promotion recommendation
    """
    if not canary_results or not baseline_results:
        return {}

    def acc_lat(results):
        tptn, n = 0, 0
        latency = 0
        for pred in results:
            y, y_hat = pred['ground_truth'], pred['prediction']
            latency += pred['latency_ms']
            if y == y_hat:
                tptn += 1
            n += 1
        if n == 0:
            return 0.0, 0.0
        return tptn / n, latency / n

    canary_accuracy, canary_avg_latency = acc_lat(canary_results)
    baseline_accuracy, baseline_avg_latency = acc_lat(baseline_results)

    accuracy_change_pct = (canary_accuracy - baseline_accuracy) / baseline_accuracy
    latency_change_pct = (canary_avg_latency - baseline_avg_latency) / baseline_avg_latency

    print(accuracy_change_pct, accuracy_tolerance, latency_change_pct, latency_tolerance)
    if -accuracy_change_pct < accuracy_tolerance and latency_change_pct < latency_tolerance:
        promote_recommended = True
    else:
        promote_recommended = False
    return {
        'canary_accuracy': round(canary_accuracy, 4),
        'baseline_accuracy': round(baseline_accuracy, 4),
        'accuracy_change_pct': round(accuracy_change_pct * 100, 2),
        'canary_avg_latency': round(canary_avg_latency, 2),
        'baseline_avg_latency': round(baseline_avg_latency, 2),
        'latency_change_pct': round(latency_change_pct * 100, 2),
        'promote_recommended': promote_recommended
    }

print(analyze_canary_deployment([{'latency_ms': 52, 'prediction': 1, 'ground_truth': 1}, {'latency_ms': 54, 'prediction': 0, 'ground_truth': 0}, {'latency_ms': 53, 'prediction': 1, 'ground_truth': 1}, {'latency_ms': 55, 'prediction': 0, 'ground_truth': 0}, {'latency_ms': 56, 'prediction': 1, 'ground_truth': 1}], [{'latency_ms': 50, 'prediction': 1, 'ground_truth': 1}, {'latency_ms': 48, 'prediction': 0, 'ground_truth': 1}, {'latency_ms': 52, 'prediction': 1, 'ground_truth': 1}, {'latency_ms': 50, 'prediction': 0, 'ground_truth': 0}, {'latency_ms': 50, 'prediction': 0, 'ground_truth': 0}]))