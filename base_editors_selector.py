wt_sequence = (input('Enter sequence for editing \n')).upper()
nucleotide = (input('Enter nucleotide for replace \n')).upper()
directory_filename = (input('Enter directory filenam \n'))
mt_sequence = wt_sequence[:30] + nucleotide + wt_sequence[31:]
mutation = wt_sequence[30] + nucleotide
f = open(directory_filename, 'w+')
f.write('>wt ' + '\n' + wt_sequence + '\n' + '>mt ' + '\n' + mt_sequence)
f.close()
def complementary_reverse_sequence(sequence):
    sequence = sequence[::-1]
    len_seq = len(sequence)
    result = ''
    for i in range(len_seq):
        if sequence[i] == 'A':
            result += 'T'
        elif sequence[i] == 'T':
            result += 'A'
        elif sequence[i] == 'C':
            result += 'G'
        elif sequence[i] == 'G':
            result += 'C'
    return result

if mutation == 'GA':
    base_editor = 'ABEs: ABE7.10'
    a, b, c, d = 17, 15, 14, 13
elif mutation == 'TC':
    base_editor = 'CBEs: Target-AID'
    a, b, c, d = 19, 17, 16, 13
elif mutation == 'AG':
    base_editor = 'ABEs: ABE7.10'
    a, b, c, d = 19, 17, 16, 13
    mt_sequence = complementary_reverse_sequence(mt_sequence)
elif mutation == 'CT':
    base_editor = 'CBEs: Target-AID'
    a, b, c, d = 17, 15, 14, 13
    mt_sequence = complementary_reverse_sequence(mt_sequence)
else:
    raise SystemExit('Base editors can not be applied')

def find_protospacer(sequence, mear, meal, lear, leal): # mea (max editor activity), lea (lower editor activity)
    x = sequence.rfind('GG', 31, -1)
    PAM = x - 1
    while PAM != -2:
        if meal <= PAM - 30 <= mear:
            return sequence[PAM - 20:PAM]
        x = sequence.rfind('GG', 31, (x - 1))
        PAM = x - 1
    x = sequence.rfind('GG', 31, -1)
    PAM = x - 1
    while PAM != -2:
        if leal <= PAM - 30 <= lear:
            return sequence[PAM - 20:PAM]
        x = sequence.rfind('GG', 31, (x - 1))
        PAM = x - 1
    return 'sequence of protospacer can not be found'

protospacer = find_protospacer(mt_sequence, a, b, c, d)
if len(protospacer) != 20:
    print(f"wt {wt_sequence}", f"mt {mt_sequence}", base_editor, f" {protospacer}", sep='\n')
else:
    print(f"wt {wt_sequence}", f"mt {mt_sequence}", base_editor, f"protospacer 5' {protospacer} 3'", sep='\n')
