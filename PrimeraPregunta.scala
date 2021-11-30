def suma(x:Int, y:Int):Int = x + y
def resta(x:Int, y:Int):Int = x - y
def multiplica(x:Int, y:Int):Int = x * y
def divide(x:Int, y:Int):Int = x / y

def calculadora(x:Int, y:Int, operacion:String):Int= {
	operacion match {
	case "suma" => suma(x,y)
	case "resta" => resta(x,y)
	case "multiplica" => multiplica(x,y)
	case "divide" => divide(x,y)
	case "" => -1
	}
}

// se llama de la siguiente forma
val resultado = calculadora(6, 7, "suma")