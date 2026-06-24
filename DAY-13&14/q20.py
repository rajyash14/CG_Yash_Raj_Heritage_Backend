def is_valid_bst(self) -> bool:
        return self._validate(self.root, None, None)

    def _validate(self, node: Optional[BSTNode], min_val: Optional[Any], max_val: Optional[Any]) -> bool:
        if node is None: 
            return True
        if (min_val is not None and node.data <= min_val) or \
           (max_val is not None and node.data >= max_val): 
            return False
        return (self._validate(node.left, min_val, node.data) and
                self._validate(node.right, node.data, max_val))