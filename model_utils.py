def to_dense(X):
    return X.toarray() if hasattr(X, 'toarray') else X
