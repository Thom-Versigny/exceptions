while True:
    try:
        getal = int(input('type een woordt: '))
    except ValueError:
        print('grapje voer een getal in')
    else:
        print(f'dit het getal dat u heeft ingevult: {getal}')
        break
    finally:
        print('dankje voor het invulen van deze test')
    
