import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print('Dimensiones:', consumo.ndim)
print('Forma:', consumo.shape)
print('Tipo de datos:', consumo.dtype)
print('Consumo primer hogar:', consumo[0])
print('Consumo el miercoles (dia 3):', consumo[:, 2])

promedio_por_hogar = np.mean(consumo, axis=1) #promedio por fila
promedio_por_dia = np.mean(consumo, axis=0) #promedio por columna
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

maximos = np.max(consumo, axis=1)
minimos = np.min(consumo, axis=0)

desviacion = np.std(consumo)
#suma por hogar semanal
consumo_total_hogar = np.sum(consumo, axis=1)

# hogar con mas consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

#hogar con menos consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

#comparar hogares mayores a 100
altos = consumo_total_hogar > 100

#filtrando hogares que cumplen la condicion
consumo_mayor_100 = np.where(altos)[0]

print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

#aplicando normalizacion MinMac al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

#resultado
print(consumo_normalizado)


consumo_hogar5_viernes = consumo[4, 4]
print("Consumo del hogar 5 el viernes:", consumo_hogar5_viernes)

consumo_ultimos3_domingo = consumo[-3:, 6]
print("Consumo de los últimos 3 hogares el domingo:", consumo_ultimos3_domingo)

consumo_finde = consumo[:, [5, 6]]
promedio_finde = np.mean(consumo_finde)
print("Promedio de consumo en fines de semana:", promedio_finde)

desviacion_dias = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desviacion_dias)
print("Desviaciones por día:", desviacion_dias)
print("Día de la semana con mayor desviación estándar:", dia_mayor_desviacion)

indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]
print("Índices de los 3 hogares con menor consumo:", indices_menor_consumo)
print("Valores de consumo total de esos hogares:", valores_menor_consumo)

hogar3_original = consumo[2]
hogar3_aumento = hogar3_original * 1.10
nuevo_total_hogar3 = np.sum(hogar3_aumento)
print("Nuevo consumo total del hogar 3 con aumento del 10%:", nuevo_total_hogar3)