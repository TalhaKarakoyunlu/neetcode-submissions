class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for astring in strs:
            s += str(len(astring))
            s += "#"
            s += astring
        return s

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        if s == "":
            return output

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            subs = s[j+1:j+1+length]
            output.append(subs)
            i = j+1+length
        
        return output