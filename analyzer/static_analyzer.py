import ast


class WorkloadAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.cpu_score = 0
        self.disk_score = 0
        self.network_score = 0

    def visit_For(self, node):
        self.cpu_score += 2
        self.generic_visit(node)

    def visit_While(self, node):
        self.cpu_score += 2
        self.generic_visit(node)

    def visit_Call(self, node):

        # Detect file operations
        if isinstance(node.func, ast.Name):
            if node.func.id in ["open", "read", "write"]:
                self.disk_score += 2

        # Detect network libraries
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ["get", "post", "connect", "send"]:
                self.network_score += 2

        self.generic_visit(node)


def analyze_script(file_path):

    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    analyzer = WorkloadAnalyzer()
    analyzer.visit(tree)

    return {
        "cpu": analyzer.cpu_score,
        "disk": analyzer.disk_score,
        "network": analyzer.network_score
    }
