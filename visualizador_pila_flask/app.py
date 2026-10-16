from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "cambia-esta-clave-en-produccion"

# Estado en memoria: adecuado para una demostración local de un solo usuario.
stack = []
capacity = None


def is_empty(items):
    """Indica si la pila no contiene elementos."""
    return len(items) == 0


def push(item):
    """Agrega un elemento si la pila todavía tiene capacidad."""
    if capacity is None:
        return False, "Primero debes configurar el tamaño de la pila."
    if len(stack) >= capacity:
        return False, "La pila está llena. No se agregó el elemento."
    stack.append(item)
    return True, f"Se agregó «{item}» a la pila."


def pop_item():
    """Retira y devuelve el elemento superior."""
    if is_empty(stack):
        return False, "La pila está vacía."
    item = stack.pop()
    return True, f"Se retiró «{item}» de la pila."


@app.route("/", methods=["GET", "POST"])
def index():
    global capacity

    if request.method == "POST":
        action = request.form.get("action", "")

        if action == "configure":
            raw_capacity = request.form.get("capacity", "").strip()
            try:
                new_capacity = int(raw_capacity)
                if new_capacity < 1:
                    raise ValueError
            except ValueError:
                flash("Ingresa un tamaño entero mayor que cero.", "danger")
            else:
                # Al configurar una nueva capacidad se reinicia la pila para
                # evitar perder elementos de forma silenciosa.
                capacity = new_capacity
                stack.clear()
                flash(f"Pila configurada con capacidad de {capacity} elementos.", "success")

        elif action == "push":
            item = request.form.get("item", "").strip()
            if not item:
                flash("Escribe un elemento antes de apilarlo.", "warning")
            else:
                ok, message = push(item)
                flash(message, "success" if ok else "danger")

        elif action == "pop":
            ok, message = pop_item()
            flash(message, "success" if ok else "warning")

        elif action == "clear":
            stack.clear()
            flash("La pila se vació correctamente.", "info")

        return redirect(url_for("index"))

    return render_template("index.html", stack=list(stack), capacity=capacity)


if __name__ == "__main__":
    app.run(debug=True)
