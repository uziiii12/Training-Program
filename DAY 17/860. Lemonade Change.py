class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fi=0
        te=0
        tw=0
        for i in bills:
            if i  ==5:
                fi+=1
            elif i  ==10:
                if fi==0:
                    return False
                fi-=1
                te+=1
            else  :
                if te> 0 and fi > 0:
                    te -= 1
                    fi -= 1

                elif fi >= 3:
                    fi -= 3

                else:
                    return False
        return True              

            
        