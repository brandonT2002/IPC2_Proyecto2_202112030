```java
public boolean buildElement(compuesto) {
    coord encontrado
    for(Elemento elemento : compuesto) {
        encontrado = getCoord(elemento)
        if (encontrado != null) {
            movePins()
        }
        else {
            return false;
        }
    }
    resetPins()
    return true;
}

public void movePins(int pinY, int elmX) {
    boolean right;
    boolean stop;
    for(Pin pin : maquina) {
        stop = pin.getCurrent().index == elmX;
        if (!top) {
            right = pin.getCurrent().index < elmX;
            while (true) {
                if (right) {
                    pin.moveRight();
                }
                else {
                    pin.moveLef();
                }
            }
            if (pin.index == pinY) {
                // fusionar
            }
        }
    }
}

public coord getCoord(elemento) {
    int index;
    for(Pin pin : maquina) {
        index = buscarE(elemento);
        if (index != -1) {
            return new coord(pin.index,index)
        }
    }
    return null;
}

// nuevo objeto
class coord {
    int pin;
    int element;
    public coord(int pin, int element) {
        this.pin = pin;
        this.element = element;
    }
}
```