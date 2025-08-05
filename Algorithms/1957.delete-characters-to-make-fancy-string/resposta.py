class Solution:
    def makeFancyString(self, s: str) -> str:
        resposta = []
        for i in s:
            if len(resposta)>=2 and resposta[-1] == resposta[-2] == i:
                continue
            resposta.append(i)
        resposta = ''.join(resposta)
        return  resposta