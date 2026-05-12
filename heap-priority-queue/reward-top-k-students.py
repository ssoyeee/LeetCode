class Solution:
    def topStudents(self, pos: List[str], neg: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        
        stud = []
        pos, neg = set(pos), set(neg)
    
        for rep, sid in zip(report, student_id):
            score = 0
            for w in rep.split(" "):
                if w in pos : score += 3
                if w in neg : score -= 1
            stud.append((-score,sid))
            
        stud.sort()
        return [sid for _, sid in stud[0:k]]