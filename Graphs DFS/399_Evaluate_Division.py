class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Given a list of equations and values, and a list of queries, calculate the result of each query.

        Each equation is a pair of strings representing the variables in the equation, and a float representing the value of the equation.
        Each query is also a pair of strings representing the variables in the query.

        The result of a query is the value of the variable on the right-hand side divided by the variable on the left-hand side,
        if the query variables are in the same connected component, and -1 otherwise.

        :param equations: A list of lists of strings, where each inner list contains two strings representing the variables in the equation
        :param values: A list of floats, where each float represents the value of the corresponding equation
        :param queries: A list of lists of strings, where each inner list contains two strings representing the variables in the query
        :return: A list of floats representing the result of each query
        
        
        Time Complexity : O(E + Q * F), where e is the number of equations, q is the number of queries.
        Space Complexity : O(V + Q), where v is the number of unique variables across all equations and queries. f is the average degree of nodes in the graph.
        """
        def find(x):
            if p[x] != x:
                origin = p[x]
                p[x] = find(p[x])
                w[x] *= w[origin]
            return p[x]

        w = defaultdict(lambda: 1)
        p = defaultdict()
        for a, b in equations:
            p[a], p[b] = a, b
        for i, v in enumerate(values):
            a, b = equations[i]
            pa, pb = find(a), find(b)
            if pa == pb:
                continue
            p[pa] = pb
            w[pa] = w[b] * v / w[a]
        return [
            -1 if c not in p or d not in p or find(c) != find(d) else w[c] / w[d]
            for c, d in queries
        ]