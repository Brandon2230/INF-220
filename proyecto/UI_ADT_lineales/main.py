import tkinter as tk
from tkinter import messagebox, ttk
import re
import math

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones con Conjuntos y Polinomios")
        self.root.geometry("1000x700")
        self.root.configure(bg='#E3F2FD')  # Fondo azul claro
        
        # Variables para almacenar conjuntos y polinomios
        self.conjuntoA = set()
        self.conjuntoB = set()
        self.polinomioP = {}
        self.polinomioQ = {}
        
        # Configurar estilo
        self.button_bg = '#2196F3'
        self.button_active_bg = '#1976D2'
        self.button_fg = 'white'
        self.font = ('Arial', 10)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame para conjuntos
        conjuntos_frame = tk.Frame(self.notebook, bg='#E3F2FD')
        self.notebook.add(conjuntos_frame, text="Operaciones con Conjuntos")
        
        # Frame para polinomios
        self.polinomios_frame = tk.Frame(self.notebook, bg='#E3F2FD')
        self.notebook.add(self.polinomios_frame, text="Operaciones con Polinomios")
        
        # ===== INTERFAZ PARA CONJUNTOS =====
        tk.Label(conjuntos_frame, text="CONJUNTOS", font=('Arial', 14, 'bold'), 
                bg='#E3F2FD', fg='#0D47A1').pack(pady=10)
        
        # Frame principal para conjuntos (dividido en izquierda y derecha)
        main_conjuntos_frame = tk.Frame(conjuntos_frame, bg='#E3F2FD')
        main_conjuntos_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame izquierdo para entrada de datos y operaciones
        left_frame = tk.Frame(main_conjuntos_frame, bg='#E3F2FD', width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Frame derecho para representación gráfica
        right_frame = tk.Frame(main_conjuntos_frame, bg='#E3F2FD')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Canvas para la representación gráfica
        self.canvas = tk.Canvas(right_frame, bg='white', width=400, height=400)
        self.canvas.pack(pady=10)
        
        # Frame para entrada de datos
        input_frame = tk.Frame(left_frame, bg='#E3F2FD')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Conjunto A (números separados por coma):", 
                bg='#E3F2FD').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_conjuntoA = tk.Entry(input_frame, width=30)
        self.entry_conjuntoA.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Conjunto B (números separados por coma):", 
                bg='#E3F2FD').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry_conjuntoB = tk.Entry(input_frame, width=30)
        self.entry_conjuntoB.grid(row=1, column=1, padx=5, pady=5)
        
        # Botón para definir conjuntos
        definir_btn = tk.Button(input_frame, text="Definir Conjuntos", command=self.definir_conjuntos,
                               bg=self.button_bg, fg=self.button_fg, font=self.font, relief=tk.FLAT)
        definir_btn.grid(row=2, column=0, columnspan=2, pady=10)
        definir_btn.bind("<Enter>", lambda e: definir_btn.configure(bg=self.button_active_bg))
        definir_btn.bind("<Leave>", lambda e: definir_btn.configure(bg=self.button_bg))
        
        # Botones para operaciones con conjuntos
        buttons_frame = tk.Frame(left_frame, bg='#E3F2FD')
        buttons_frame.pack(pady=10)
        
        conjunto_buttons = [
            ("Unión (A ∪ B)", self.union_conjuntos),
            ("Intersección (A ∩ B)", self.interseccion_conjuntos),
            ("Diferencia (A - B)", self.diferencia_conjuntos),
            ("Diferencia (B - A)", self.diferencia_conjuntos_BA),
            ("Diferencia Simétrica", self.diferencia_simetrica),
            ("Mostrar Conjuntos", self.mostrar_conjuntos)
        ]
        
        for i, (text, command) in enumerate(conjunto_buttons):
            btn = tk.Button(buttons_frame, text=text, command=command, 
                           bg=self.button_bg, fg=self.button_fg, font=self.font,
                           relief=tk.FLAT, width=20)
            btn.grid(row=i, column=0, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=self.button_active_bg))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=self.button_bg))
        
        # Área de resultados para conjuntos
        tk.Label(left_frame, text="Resultados:", font=('Arial', 12, 'bold'), 
                bg='#E3F2FD').pack(pady=(20, 5))
        
        self.resultado_conjuntos = tk.Text(left_frame, height=8, width=40)
        self.resultado_conjuntos.pack(pady=5, padx=10)
        
        # ===== INTERFAZ PARA POLINOMIOS =====
        tk.Label(self.polinomios_frame, text="POLINOMIOS", font=('Arial', 14, 'bold'), 
                bg='#E3F2FD', fg='#0D47A1').pack(pady=10)
        
        # Frame para entrada de polinomios
        poly_input_frame = tk.Frame(self.polinomios_frame, bg='#E3F2FD')
        poly_input_frame.pack(pady=10)
        
        tk.Label(poly_input_frame, text="Polinomio P(x) (ej: 3x^2 + 2x - 1):", 
                bg='#E3F2FD').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_polinomioP = tk.Entry(poly_input_frame, width=40)
        self.entry_polinomioP.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(poly_input_frame, text="Polinomio Q(x) (ej: x^2 - 4x + 5):", 
                bg='#E3F2FD').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entry_polinomioQ = tk.Entry(poly_input_frame, width=40)
        self.entry_polinomioQ.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame para evaluación de polinomios
        eval_frame = tk.Frame(self.polinomios_frame, bg='#E3F2FD')
        eval_frame.pack(pady=10)
        
        tk.Label(eval_frame, text="Valor de x para evaluar:", 
                bg='#E3F2FD').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entry_valor_x = tk.Entry(eval_frame, width=10)
        self.entry_valor_x.grid(row=0, column=1, padx=5, pady=5)
        
        # Botones para operaciones con polinomios
               # Botones para operaciones con polinomios
        self.poly_buttons_frame = tk.Frame(self.polinomios_frame, bg='#E3F2FD')
        self.poly_buttons_frame.pack(pady=10)
        
        polinomio_buttons = [
            ("Definir Polinomios", self.definir_polinomios),
            ("Sumar P(x) + Q(x)", self.sumar_polinomios),
            ("Restar P(x) - Q(x)", self.restar_polinomios),
            ("Multiplicar P(x) * Q(x)", self.multiplicar_polinomios),
            ("Evaluar P(x)", lambda: self.evaluar_polinomio('P')),
            ("Evaluar Q(x)", lambda: self.evaluar_polinomio('Q')),
            ("Mostrar Polinomios", self.mostrar_polinomios),
            ("Evaluar Suma/Resta/Multiplicación", self.evaluar_operaciones_polinomios)
        ]
        
        for i, (text, command) in enumerate(polinomio_buttons):
            btn = tk.Button(self.poly_buttons_frame, text=text, command=command, 
                           bg=self.button_bg, fg=self.button_fg, font=self.font,
                           relief=tk.FLAT, width=20)
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=self.button_active_bg))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=self.button_bg))
        # Área de resultados para polinomios
        tk.Label(self.polinomios_frame, text="Resultados:", font=('Arial', 12, 'bold'), 
                bg='#E3F2FD').pack(pady=(20, 5))

        self.resultado_polinomios = tk.Text(self.polinomios_frame, height=10, width=70)
        self.resultado_polinomios.pack(pady=5, padx=10)
    
    def evaluar_operaciones_polinomios(self):
        """Evalúa la suma, resta y multiplicación de P(x) y Q(x) en el valor de x ingresado"""
        try:
            valor_x_str = self.entry_valor_x.get()
            if not valor_x_str:
                messagebox.showwarning("Advertencia", "Debe ingresar un valor para x")
                return
            x = float(valor_x_str)
            if not self.polinomioP or not self.polinomioQ:
                messagebox.showwarning("Advertencia", "Primero debe definir ambos polinomios.")
                return
            # Suma
            suma = {}
            for exp, coef in self.polinomioP.items():
                suma[exp] = coef
            for exp, coef in self.polinomioQ.items():
                if exp in suma:
                    suma[exp] += coef
                else:
                    suma[exp] = coef
            suma = {exp: coef for exp, coef in suma.items() if coef != 0}
            resultado_suma = sum(coef * (x ** exp) for exp, coef in suma.items())
            # Resta
            resta = {}
            for exp, coef in self.polinomioP.items():
                resta[exp] = coef
            for exp, coef in self.polinomioQ.items():
                if exp in resta:
                    resta[exp] -= coef
                else:
                    resta[exp] = -coef
            resta = {exp: coef for exp, coef in resta.items() if coef != 0}
            resultado_resta = sum(coef * (x ** exp) for exp, coef in resta.items())
            # Multiplicación
            multiplicacion = {}
            for expP, coefP in self.polinomioP.items():
                for expQ, coefQ in self.polinomioQ.items():
                    exp = expP + expQ
                    coef = coefP * coefQ
                    if exp in multiplicacion:
                        multiplicacion[exp] += coef
                    else:
                        multiplicacion[exp] = coef
            multiplicacion = {exp: coef for exp, coef in multiplicacion.items() if coef != 0}
            resultado_multiplicacion = sum(coef * (x ** exp) for exp, coef in multiplicacion.items())
            texto = f"Evaluación en x = {x}\n\n"
            texto += f"P(x) = {self.polinomio_a_texto(self.polinomioP)}\n"
            texto += f"Q(x) = {self.polinomio_a_texto(self.polinomioQ)}\n\n"
            texto += f"[P(x) + Q(x)]({x}) = {resultado_suma}\n"
            texto += f"[P(x) - Q(x)]({x}) = {resultado_resta}\n"
            texto += f"[P(x) * Q(x)]({x}) = {resultado_multiplicacion}"
            self.mostrar_resultado_polinomios(texto)
        except ValueError:
            messagebox.showerror("Error", "El valor de x debe ser un número válido")
        except Exception as e:
            messagebox.showerror("Error", f"Error al evaluar las operaciones: {str(e)}")
    
    # ===== MÉTODOS PARA CONJUNTOS =====
    def convertir_a_numeros_ordenados(self, conjunto):
        """Convierte un conjunto de strings a números y los ordena"""
        try:
            numeros = []
            for elemento in conjunto:
                try:
                    # Intentar convertir a entero
                    numeros.append(int(elemento))
                except ValueError:
                    try:
                        # Si no es entero, intentar convertir a float
                        numeros.append(float(elemento))
                    except ValueError:
                        # Si no es número, mantener como string
                        numeros.append(elemento)
            
            # Ordenar si todos son números, de lo contrario ordenar alfabéticamente
            if all(isinstance(x, (int, float)) for x in numeros):
                return sorted(numeros)
            else:
                return sorted(numeros, key=str)
        except:
            # Si hay error, devolver el conjunto original ordenado como strings
            return sorted(conjunto, key=str)
    
    def definir_conjuntos(self):
        try:
            # Obtener y procesar conjunto A
            textoA = self.entry_conjuntoA.get()
            elementosA = [elem.strip() for elem in textoA.split(',') if elem.strip()]
            self.conjuntoA = set(elementosA)
            
            # Obtener y procesar conjunto B
            textoB = self.entry_conjuntoB.get()
            elementosB = [elem.strip() for elem in textoB.split(',') if elem.strip()]
            self.conjuntoB = set(elementosB)
            
            self.mostrar_resultado_conjuntos("Conjuntos definidos correctamente.")
            self.dibujar_conjuntos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al definir conjuntos: {str(e)}")
    
    def dibujar_conjuntos(self):
        """Dibuja los conjuntos en el canvas como diagramas de Venn"""
        self.canvas.delete("all")
        
        if not self.conjuntoA and not self.conjuntoB:
            return
        
        # Coordenadas y dimensiones
        width = 400
        height = 400
        center_x = width // 2
        center_y = height // 2
        radius = 120
        
        # Dibujar círculo A (izquierda)
        circleA_x = center_x - radius // 2
        self.canvas.create_oval(circleA_x - radius, center_y - radius,
                               circleA_x + radius, center_y + radius,
                               outline='#2196F3', width=2, fill='#E3F2FD')
        
        # Dibujar círculo B (derecha)
        circleB_x = center_x + radius // 2
        self.canvas.create_oval(circleB_x - radius, center_y - radius,
                               circleB_x + radius, center_y + radius,
                               outline='#F44336', width=2, fill='#FFEBEE')
        
        # Etiquetas
        self.canvas.create_text(circleA_x - radius + 20, center_y - radius + 20, 
                               text="A", font=('Arial', 14, 'bold'), fill='#0D47A1')
        self.canvas.create_text(circleB_x + radius - 20, center_y - radius + 20, 
                               text="B", font=('Arial', 14, 'bold'), fill='#B71C1C')
        
        # Convertir elementos a números si es posible y ordenarlos
        elementosA_ordenados = self.convertir_a_numeros_ordenados(self.conjuntoA)
        elementosB_ordenados = self.convertir_a_numeros_ordenados(self.conjuntoB)
        
        # Dibujar elementos del conjunto A (solo en A)
        onlyA = self.conjuntoA - self.conjuntoB
        onlyA_ordenados = self.convertir_a_numeros_ordenados(onlyA)
        for i, elemento in enumerate(onlyA_ordenados):
            if i < 8:  # Limitar a 8 elementos para no saturar
                y_pos = center_y - radius + 50 + i * 25
                self.canvas.create_text(circleA_x - radius + 30, y_pos, 
                                       text=str(elemento), font=('Arial', 10), fill='#0D47A1')
        
        # Dibujar elementos del conjunto B (solo en B)
        onlyB = self.conjuntoB - self.conjuntoA
        onlyB_ordenados = self.convertir_a_numeros_ordenados(onlyB)
        for i, elemento in enumerate(onlyB_ordenados):
            if i < 8:  # Limitar a 8 elementos para no saturar
                y_pos = center_y - radius + 50 + i * 25
                self.canvas.create_text(circleB_x + radius - 30, y_pos, 
                                       text=str(elemento), font=('Arial', 10), fill='#B71C1C')
        
        # Dibujar elementos de la intersección (A ∩ B)
        interseccion = self.conjuntoA & self.conjuntoB
        interseccion_ordenados = self.convertir_a_numeros_ordenados(interseccion)
        for i, elemento in enumerate(interseccion_ordenados):
            if i < 8:  # Limitar a 8 elementos para no saturar
                y_pos = center_y - radius + 50 + i * 25
                self.canvas.create_text(center_x, y_pos, 
                                       text=str(elemento), font=('Arial', 10, 'bold'), fill='#4CAF50')
    
    def union_conjuntos(self):
        if not self.conjuntoA or not self.conjuntoB:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos conjuntos.")
            return
        
        resultado = self.conjuntoA.union(self.conjuntoB)
        resultado_ordenado = self.convertir_a_numeros_ordenados(resultado)
        self.mostrar_resultado_conjuntos(f"Unión A ∪ B = {resultado_ordenado}")
        self.dibujar_operacion("Unión", resultado_ordenado)
    
    def interseccion_conjuntos(self):
        if not self.conjuntoA or not self.conjuntoB:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos conjuntos.")
            return
        
        resultado = self.conjuntoA.intersection(self.conjuntoB)
        resultado_ordenado = self.convertir_a_numeros_ordenados(resultado)
        self.mostrar_resultado_conjuntos(f"Intersección A ∩ B = {resultado_ordenado}")
        self.dibujar_operacion("Intersección", resultado_ordenado)
    
    def diferencia_conjuntos(self):
        if not self.conjuntoA or not self.conjuntoB:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos conjuntos.")
            return
        
        resultado = self.conjuntoA - self.conjuntoB
        resultado_ordenado = self.convertir_a_numeros_ordenados(resultado)
        self.mostrar_resultado_conjuntos(f"Diferencia A - B = {resultado_ordenado}")
        self.dibujar_operacion("Diferencia A-B", resultado_ordenado)
    
    def diferencia_conjuntos_BA(self):
        if not self.conjuntoA or not self.conjuntoB:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos conjuntos.")
            return
        
        resultado = self.conjuntoB - self.conjuntoA
        resultado_ordenado = self.convertir_a_numeros_ordenados(resultado)
        self.mostrar_resultado_conjuntos(f"Diferencia B - A = {resultado_ordenado}")
        self.dibujar_operacion("Diferencia B-A", resultado_ordenado)
    
    def diferencia_simetrica(self):
        if not self.conjuntoA or not self.conjuntoB:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos conjuntos.")
            return
        
        resultado = self.conjuntoA.symmetric_difference(self.conjuntoB)
        resultado_ordenado = self.convertir_a_numeros_ordenados(resultado)
        self.mostrar_resultado_conjuntos(f"Diferencia Simétrica = {resultado_ordenado}")
        self.dibujar_operacion("Diferencia Simétrica", resultado_ordenado)
    
    def mostrar_conjuntos(self):
        A_ordenado = self.convertir_a_numeros_ordenados(self.conjuntoA)
        B_ordenado = self.convertir_a_numeros_ordenados(self.conjuntoB)
        
        texto = f"Conjunto A: {A_ordenado}\n"
        texto += f"Conjunto B: {B_ordenado}\n"
        texto += f"Cardinalidad de A: {len(self.conjuntoA)}\n"
        texto += f"Cardinalidad de B: {len(self.conjuntoB)}"
        self.mostrar_resultado_conjuntos(texto)
        self.dibujar_conjuntos()
    
    def dibujar_operacion(self, operacion, elementos):
        """Dibuja el resultado de una operación en el canvas"""
        self.canvas.delete("all")
        
        width = 400
        height = 400
        center_x = width // 2
        center_y = height // 2
        
        # Dibujar título de la operación
        self.canvas.create_text(center_x, 30, text=operacion, 
                               font=('Arial', 16, 'bold'), fill='#0D47A1')
        
        # Dibujar círculo para el resultado
        radio = 150
        self.canvas.create_oval(center_x - radio, center_y - radio,
                               center_x + radio, center_y + radio,
                               outline='#4CAF50', width=3, fill='#E8F5E9')
        
        # Dibujar elementos ordenados
        for i, elemento in enumerate(elementos):
            if i < 12:  # Limitar a 12 elementos para no saturar
                angulo = 2 * 3.1416 * i / min(len(elementos), 12)
                x = center_x + int((radio - 30) * 0.8 * math.cos(angulo))
                y = center_y + int((radio - 30) * 0.8 * math.sin(angulo))
                
                # Dibujar círculo alrededor del elemento
                self.canvas.create_oval(x-20, y-15, x+20, y+15, 
                                       fill='#4CAF50', outline='#2E7D32')
                
                # Dibujar el elemento
                self.canvas.create_text(x, y, text=str(elemento), 
                                       font=('Arial', 10, 'bold'), fill='white')
    
    def mostrar_resultado_conjuntos(self, texto):
        self.resultado_conjuntos.delete(1.0, tk.END)
        self.resultado_conjuntos.insert(tk.END, texto)
    
    # ===== MÉTODOS PARA POLINOMIOS =====
    def parse_polinomio(self, texto):
        """Convierte un string de polinomio a un diccionario de coeficientes"""
        polinomio = {}
        
        # Patrón para encontrar términos: coeficiente (opcional), x (opcional), exponente (opcional)
        patron = r'([+-]?\s*\d*)\s*x\s*(\^\s*(\d+))?|([+-]?\s*\d+)'
        
        # Encontrar todos los términos
        terminos = re.findall(patron, texto)
        
        for term in terminos:
            coef_str, _, exp_str, constante = term
            
            # Procesar coeficiente
            if coef_str.strip() in ['', '+']:
                coef = 1
            elif coef_str.strip() == '-':
                coef = -1
            else:
                coef = float(coef_str.replace(' ', ''))
            
            # Procesar exponente
            if exp_str:
                exp = int(exp_str)
            elif coef_str or term[0]:  # Hay x pero sin exponente explícito
                exp = 1
            else:  # Es una constante
                exp = 0
                if constante:
                    coef = float(constante.replace(' ', ''))
            
            # Sumar al coeficiente existente si ya hay términos con ese exponente
            if exp in polinomio:
                polinomio[exp] += coef
            else:
                polinomio[exp] = coef
        
        return polinomio

    def polinomio_a_texto(self, polinomio):
        """Convierte un diccionario de coeficientes a string de polinomio"""
        terminos = []
        for exp in sorted(polinomio.keys(), reverse=True):
            coef = polinomio[exp]
            if coef == 0:
                continue
            
            signo = '+' if coef > 0 else '-'
            abs_coef = abs(coef)
            
            if exp == 0:
                termino = f"{signo} {abs_coef}"
            elif exp == 1:
                if abs_coef == 1:
                    termino = f"{signo} x"
                else:
                    termino = f"{signo} {abs_coef}x"
            else:
                if abs_coef == 1:
                    termino = f"{signo} x^{exp}"
                else:
                    termino = f"{signo} {abs_coef}x^{exp}"
            
            terminos.append(termino)
        
        # Unir términos y ajustar el primer término
        if not terminos:
            return "0"
        
        expresion = " ".join(terminos)
        if expresion.startswith("+ "):
            expresion = expresion[2:]
        return expresion
    
    def evaluar_polinomio(self, polinomio_id):
        """Evalúa un polinomio en un valor específico de x"""
        try:
            # Obtener el valor de x
            valor_x_str = self.entry_valor_x.get()
            if not valor_x_str:
                messagebox.showwarning("Advertencia", "Debe ingresar un valor para x")
                return
                
            x = float(valor_x_str)
            
            # Seleccionar el polinomio a evaluar
            if polinomio_id == 'P':
                polinomio = self.polinomioP
                nombre = "P(x)"
            else:
                polinomio = self.polinomioQ
                nombre = "Q(x)"
            
            if not polinomio:
                messagebox.showwarning("Advertencia", f"Primero debe definir el polinomio {nombre}")
                return
            
            # Evaluar el polinomio
            resultado = 0
            for exp, coef in polinomio.items():
                resultado += coef * (x ** exp)
            
            # Mostrar el resultado
            texto = f"Evaluación de {nombre} en x = {x}\n\n"
            texto += f"{nombre} = {self.polinomio_a_texto(polinomio)}\n"
            texto += f"{nombre.replace('(x)', f'({x})')} = {resultado}"
            
            self.mostrar_resultado_polinomios(texto)
            
        except ValueError:
            messagebox.showerror("Error", "El valor de x debe ser a number")
        except Exception as e:
            messagebox.showerror("Error", f"Error al evaluar el polinomio: {str(e)}")
    
    def definir_polinomios(self):
        try:
            textoP = self.entry_polinomioP.get()
            textoQ = self.entry_polinomioQ.get()
            
            self.polinomioP = self.parse_polinomio(textoP)
            self.polinomioQ = self.parse_polinomio(textoQ)
            
            self.mostrar_resultado_polinomios("Polinomios definidos correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al definir polinomios: {str(e)}")
    
    def sumar_polinomios(self):
        if not self.polinomioP or not self.polinomioQ:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos polinomios.")
            return
        
        resultado = {}
        # Sumar todos los términos de P
        for exp, coef in self.polinomioP.items():
            resultado[exp] = coef
        
        # Sumar todos los términos de Q
        for exp, coef in self.polinomioQ.items():
            if exp in resultado:
                resultado[exp] += coef
            else:
                resultado[exp] = coef
        
        # Eliminar términos con coeficiente cero
        resultado = {exp: coef for exp, coef in resultado.items() if coef != 0}
        
        texto_resultado = f"P(x) = {self.polinomio_a_texto(self.polinomioP)}\n"
        texto_resultado += f"Q(x) = {self.polinomio_a_texto(self.polinomioQ)}\n"
        texto_resultado += f"P(x) + Q(x) = {self.polinomio_a_texto(resultado)}"
        
        self.mostrar_resultado_polinomios(texto_resultado)
    
    def restar_polinomios(self):
        if not self.polinomioP or not self.polinomioQ:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos polinomios.")
            return
        
        resultado = {}
        # Sumar todos los términos de P
        for exp, coef in self.polinomioP.items():
            resultado[exp] = coef
        
        # Restar todos los términos de Q
        for exp, coef in self.polinomioQ.items():
            if exp in resultado:
                resultado[exp] -= coef
            else:
                resultado[exp] = -coef
        
        # Eliminar términos con coeficiente cero
        resultado = {exp: coef for exp, coef in resultado.items() if coef != 0}
        
        texto_resultado = f"P(x) = {self.polinomio_a_texto(self.polinomioP)}\n"
        texto_resultado += f"Q(x) = {self.polinomio_a_texto(self.polinomioQ)}\n"
        texto_resultado += f"P(x) - Q(x) = {self.polinomio_a_texto(resultado)}"
        
        self.mostrar_resultado_polinomios(texto_resultado)
    
    def multiplicar_polinomios(self):
        if not self.polinomioP or not self.polinomioQ:
            messagebox.showwarning("Advertencia", "Primero debe definir ambos polinomios.")
            return
        
        resultado = {}
        # Multiplicar cada término de P por cada término de Q
        for expP, coefP in self.polinomioP.items():
            for expQ, coefQ in self.polinomioQ.items():
                exp = expP + expQ
                coef = coefP * coefQ
                
                if exp in resultado:
                    resultado[exp] += coef
                else:
                    resultado[exp] = coef
        
        # Eliminar términos con coeficiente cero
        resultado = {exp: coef for exp, coef in resultado.items() if coef != 0}
        
        texto_resultado = f"P(x) = {self.polinomio_a_texto(self.polinomioP)}\n"
        texto_resultado += f"Q(x) = {self.polinomio_a_texto(self.polinomioQ)}\n"
        texto_resultado += f"P(x) * Q(x) = {self.polinomio_a_texto(resultado)}"
        
        self.mostrar_resultado_polinomios(texto_resultado)
    
    def mostrar_polinomios(self):
        texto = f"P(x) = {self.polinomio_a_texto(self.polinomioP)}\n"
        texto += f"Q(x) = {self.polinomio_a_texto(self.polinomioQ)}"
        self.mostrar_resultado_polinomios(texto)
    
    def mostrar_resultado_polinomios(self, texto):
        self.resultado_polinomios.delete(1.0, tk.END)
        self.resultado_polinomios.insert(tk.END, texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()