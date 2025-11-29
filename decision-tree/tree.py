class DecisionTree:

    def __init__(self, criterion='gini', splitter='best', max_depth=5, min_samples_split=2,
                 min_samples_leaf=1, min_weight_fraction_leaf=0, max_features='auto', random_state=42, 
                 max_leaf_nodes=None, min_impurity_decrease=0, class_weight=None, ccp_alpha=0, monotonic_cst=None):
        
        self.criterion=criterion, # gini, entropy, log-loss
        self.splitter=splitter, # best, random
        self.max_depth=max_depth,
        self.min_samples_split=min_samples_split,
        self.min_samples_leaf=min_samples_leaf,
        self.min_weight_fraction_leaf=min_weight_fraction_leaf,
        self.max_features=max_features, # log2, auto
        self.random_state=random_state,
        self.max_leaf_nodes=max_leaf_nodes,
        self.min_impurity_decrease=min_impurity_decrease,
        self.class_weight=class_weight,
        self.ccp_alpha=ccp_alpha
        self.monotonic_cst=monotonic_cst

    def fit(self, X, y):

        pass

    def predict(self, X, y=None):

        pass

