from avoxtun import onePayment, monthlyPayment
from lanUtreikn import lanUtreikn

def main():                   
    for i in range(0,15) :
        a = 5000 * (i*3)
        b = 100 * i
        c = 12 * i
        d = 2.50 * (i*1.5)
        
        if (i%2 == 0) : e = False
        else : e = True

        print('-----------------')
        print('Test {}'.format(i+1))
        print('')
        print('Innistaeda: {}'.format(a))
        print('Innborgun: {}'.format(b))
        print('timi i fjolda manada: {}'.format(c))
        print('vextir i prosentu: {}'.format(d))
        print('Verdtrygging: {}'.format(e))
        print('')
        print('Sparnadarreikningur - ein greidsla:')
        print(onePayment(a,b,c,d,e))
        print('')
        print('Sparnadarreikningur - manadarleg greidsla:')
        print(monthlyPayment(a,b,c,d,e))
        print('')
        print('Throun lans:')
        print(lanUtreikn(a,b,c,d,e))

        
main()