class Solution:
    def isNumber(self, s: str) -> bool:
        reg = '(\s*(-|\+)?((\d*\.?\d+)|(\d+\.?\d*))(e(-|\+)?\d+)?\s*)'
        return re.fullmatch(reg,s)
