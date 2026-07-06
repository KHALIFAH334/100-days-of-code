#This is the 3rd test of my understanding of boolean logic in python. 
#This script is an automated Pull request approval gate for a development team"s repository. The script must decide whether a code branchis allowed to merge into the main code base.

peer_approvals = int(input('How many peer approvals does this PR have? (Enter a number): '))
senior_approved = input('Has a senior developer approved this PR? (True/False): ')
merge_conflict = input('Does this PR have any merge conflicts? (True/False): ')
Senior = (senior_approved.lower() == 'true')
Merge = (merge_conflict.lower() == 'true')

if ((peer_approvals >= 2) or (peer_approvals >= 1 and Senior)) and not Merge:
    print ('Merge Approved')
else:
    print ('Merge Denied')