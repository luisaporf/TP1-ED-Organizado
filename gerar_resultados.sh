programa="./obj/bin/pa1.out"
arquivo_saida="resultados.csv"

> $arquivo_saida

echo "iteracao,alg,alg,seed,seed,size,size,time,time,cmp,cmp,move,move,calls,calls" >> $arquivo_saida

iteracao=1
for alg in s i q q3 qi q3i h rs b m c bu rx  # Loop para letras especificadas
do
    for i in {1..260}
    do
        t=0  # Define o valor de t como 0
        output=$(./obj/bin/pa1.out -z $i -s 32 -a $alg -t $t)
        # Processa a saída para remover as colunas duplicadas e redireciona para o arquivo .csv
        echo "$iteracao,$output" | tr ' ' ',' >> $arquivo_saida
        iteracao=$((iteracao+1))
    done
done
