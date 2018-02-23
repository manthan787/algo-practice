# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

def solution(S):
    hour, minute = S.split(":")
    unique_digits = set([d for d in hour] + [d for d in minute])
    next_minute = next_number(unique_digits, int(minute), 59)
    if next_minute != -1: return "%s:%02d" %(hour, next_minute)
    next_hour = next_number(unique_digits, int(hour), 23)
    print next_hour
    if next_hour != -1: return "%02d:%s" %(next_hour, minute)
    return "%02d:%02d" %(next_number(unique_digits, 19, 23), next_number(unique_digits, 00, 59))

def next_number(l, ref, limit):
    """ Given a list `l` of characters returns all possible permutations
        of numbers that can be created if the number is less than given
        number `limit`
    """
    min_next = sys.maxint
    for char in l:
        for second_char in l:
            number = int(char + second_char)
            if all([number < limit, number > ref, number < min_next]):
                min_next = number
    if min_next == sys.maxint: return -1
    return min_next

print solution("23:59")

TreeSet<Integer> set = new TreeSet<>();
        int i=0;
        for (int n:flowers){
            set.add(n);
            int prev=n-k-1,next=n+k+1;

            if (set.contains(prev)){
                Integer prevNext=set.ceiling(prev+1);
                if (prevNext!=null&&prevNext==n)return set.size();
            }
            if (set.contains(next)){
                Integer nextPrev=set.floor(next-1);
                if (nextPrev!=null&&nextPrev==n)return set.size();
            }
        }
        return -1;