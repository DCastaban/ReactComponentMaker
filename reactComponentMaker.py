filename = input()

with open(filename + '.js', 'w') as f:
    f.write('class ' + filename + ' extends React.Component {\n')
    f.write('}\n')
with open(filename + '.css', 'w') as f:
    f.write('\n')


