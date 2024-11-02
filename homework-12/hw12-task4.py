def merge_sorted_list(list1,list2):
    merged_list = []
    i,j = 0,0
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            merged_list.append(list1[i])
            i+=1
        else:
            merged_list.append(list2[j])
            j+=1
    while i<len(list1):
        merged_list.append(list1[i])
        i+=1
    while j<len(list2):
        merged_list.append(list2[j])
        j+=1
    return merged_list
if __name__=="__main__":
    list1=[0,2,5]
    list2=[1,3,5,7,9]
    final_list=merge_sorted_list(list1,list2)
    print('merged final list is-',final_list)