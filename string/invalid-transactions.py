from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        name_map = defaultdict(list)
        result = []
        # parsing
        for t in transactions:
            name, time, amount, city = t.split(',')
            name_map[name].append((int(time), int(amount), city, t))
        
        # checking
        for t in transactions:
            name, time, amount, city = t.split(',')
            time, amount = int(time), int(amount)    
        
            invalid = False
            if amount > 1000:
                invalid = True
            else:
                for another_time, another_amount, another_city, _ in name_map[name]: 
                    if abs(time-another_time) <= 60 and city != another_city:
                        invalid = True
                        break
        
            if invalid:
                result.append(t)
            
        return result

        # T: O(N^2) -- for each transaction, compare with all same-name transactions
        # S: O(N) -- name_map stores all transactions