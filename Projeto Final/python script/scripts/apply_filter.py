def monta_kernel(matriz_kernel):
    kernel = [bin(pixel)[2:].zfill(8) for linha in matriz_kernel for pixel in linha]
    with open('kernel.txt', 'w') as file:
        file.write("\n".join(kernel))

def filtro_pixel(matriz_file, kernel_file):
    mem = []
    kernel = []
    with open(matriz_file, 'r') as file:
        for linha in file:
            mem.append(int(linha, 2))

    with open(kernel_file, 'r') as file:
        for linha in file:
            kernel.append(int(linha, 2))

    mem_saida = ['255']*(600*600)

    linha = 1
    pronto = 0

    while linha < 601:
        coluna = 1
        while coluna < 601:
            soma = 0
            i = 0
            deslocaLinha = -1
            deslocaColuna = -1
            while i < 9:
                k = kernel[i]
                m = mem[(linha + deslocaLinha)*602 + (coluna + deslocaColuna)]
                res = k*m
                input(f"{k}*{m} = {res}")
                res = bin(res)
                res = res[2: len(res)].zfill(8)
                resb = res[0:len(res)-4].zfill(8)
                resi = int(resb, 2)
                # input(f"{soma} - {somab} - {somai}")
                soma += resi
                i += 1
                deslocaColuna += 1

                if deslocaColuna > 1:
                    deslocaColuna = -1
                    deslocaLinha += 1
            # print(soma)
            soma = bin(soma)
            # input(f"{soma} - {soma[2:len(soma)].zfill(8)}")
            soma = soma[2:len(soma)].zfill(8)
            mem_saida[(linha-1)*600 + (coluna-1)] = soma

            coluna += 1
        linha += 1
    pronto = 1
    
    # apenas escrevendo memória no arquivo
    with open('matriz/matriz_filtrada.txt', 'w') as arquivo:
        arquivo.write("\n".join(mem_saida))
    