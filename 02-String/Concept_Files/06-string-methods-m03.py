# String operations - strip, rstrip, replace, split

voice = '   YUJI ITADORI !!!    '

print(voice.strip())                    # White space gone!
print(voice.rstrip('! '))               # Strip exclaimation
print(voice.replace('!!!', 'GONE!'))    # Replace string
print('YUJI ITADORI'.split(' '))        # Conversion to list