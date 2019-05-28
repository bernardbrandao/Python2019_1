class clone:

    def nova_lista(uma_lista):
        """ Essa funcao faz uma copia da lista dada e modifica a copia dobrando os valores dos seus elementos.
        """
        clone_lista = uma_lista[:]
        for (i, valor) in enumerate(clone_lista):
            novo_elem = 2 * valor
            clone_lista[i] = novo_elem

        return clone_lista


if __name__ == '__main__':
    minha_lista = [2, 4, 6]
    print(minha_lista)
    print(nova_lista(minha_lista))


