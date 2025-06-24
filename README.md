# Análisis Exploratorio de Rotación de Personal (HR Analytics)

Este proyecto analiza los factores que influyen en la rotación de empleados utilizando un dataset realista de IBM. El objetivo es brindar una visión clara del comportamiento de empleados que han dejado la empresa, ayudando así a identificar oportunidades para mejorar la retención.

## Dataset

- **Fuente:** IBM HR Analytics Employee Attrition Dataset
- **Registros:** 1,470 empleados
- **Variables clave:** Edad, antigüedad, ingreso, satisfacción, horas extra, puesto

El dataset original está disponible en:  
[IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

## Objetivos del análisis

- Explorar distribuciones generales de variables personales y laborales.
- Comparar características entre empleados que renunciaron vs. los que permanecen.
- Identificar patrones visibles que justifiquen acciones por parte de Recursos Humanos.

## Herramientas utilizadas

- Python (pandas, matplotlib, seaborn)
- VS Code
- Visualización de datos
- Limpieza y transformación básica

## Estructura del proyecto

```
hr-attrition-analysis/
├── data/
├── notebooks/
│ └── eda_hr_attrition.ipynb
├── images/
├── README.md
└── requirements.txt
```

## Insights clave

- Los empleados que renuncian tienden a ser más jóvenes y con menor antigüedad.
- La rotación es mayor en roles operativos y entre quienes hacen horas extra.
- Los solteros y quienes viajan con frecuencia presentan mayor riesgo de salida.
- Hay diferencias significativas en ingresos, promoción y carga laboral entre quienes se quedan y quienes se van.

## Vistas previas

<img src="[images/attrition_boxplot.png](https://github.com/civera08/hr-attrition-analysis/blob/main/Distribucion_Abandono_Categoria.png)" width="600">
<img src="[images/attrition_rate_overtime.png](https://github.com/civera08/hr-attrition-analysis/blob/main/Matriz_Correlacion_Variable.png)" width="600">

---

## Conclusiones del Análisis

Este análisis exploratorio nos permitió identificar tendencias relevantes para la gestión del talento:

- **Edad y experiencia**: La rotación es más alta entre los empleados jóvenes y con menor antigüedad.
- **Sobrecarga y horarios**: Aquellos que hacen horas extra están significativamente más expuestos a renunciar.
- **Rol y área**: Ciertos puestos operativos, como técnicos de laboratorio y vendedores, presentan mayor rotación.
- **Factores personales**: Los empleados solteros y quienes viven lejos tienen mayores tasas de salida.

## Estos hallazgos pueden ser utilizados para enfocar estrategias de retención más efectivas, como mejorar la flexibilidad laboral, optimizar procesos de promoción interna y brindar seguimiento más cercano a perfiles de riesgo.

## Contacto

Email: civera.ds@outlook.com
LinkedIn: https://linkedin.com/in/civera/
GitHub: https://github.com/civera08

---

## Licencia

Este proyecto está licenciado bajo los términos de la [Licencia MIT](LICENSE).
