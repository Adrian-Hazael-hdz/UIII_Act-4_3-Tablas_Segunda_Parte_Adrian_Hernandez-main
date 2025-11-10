from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Pedido

def inicio_PChop(request):
    return render(request, 'inicio.html')

def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        slug = request.POST.get('slug')
        prioridad = request.POST.get('prioridad')
        
        # Manejar la imagen - ESTA LÍNEA ES IMPORTANTE
        imagen = request.FILES.get('imagen')  # Usar FILES en lugar de POST
        
        categoria = Categoria(
            nombre=nombre,
            descripcion=descripcion,
            slug=slug,
            prioridad=prioridad
        )
        
        if imagen:
            categoria.imagen = imagen
            
        categoria.save()
        return redirect('ver_categorias')
    
    return render(request, 'categoria/agregar_categoria.html')

def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/ver_categorias.html', {'categorias': categorias})

def actualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.slug = request.POST.get('slug')
        categoria.prioridad = request.POST.get('prioridad')
        
        # MANEJAR LA NUEVA IMAGEN - ESTO ES IMPORTANTE
        nueva_imagen = request.FILES.get('imagen')  # Usar FILES, no POST
        if nueva_imagen:
            # Eliminar la imagen anterior si existe
            if categoria.imagen:
                categoria.imagen.delete(save=False)
            categoria.imagen = nueva_imagen
            
        categoria.save()
        return redirect('ver_categorias')
    
    return render(request, 'categoria/actualizar_categoria.html', {'categoria': categoria})

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    
    return render(request, 'categoria/borrar_categoria.html', {'categoria': categoria})

# VISTAS PARA PRODUCTO
def agregar_producto(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        marca = request.POST.get('marca')
        imagen = request.FILES.get('imagen')
        
        categoria = Categoria.objects.get(id=categoria_id)
        
        producto = Producto(
            categoria=categoria,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            marca=marca
        )
        
        if imagen:
            producto.imagen = imagen
            
        producto.save()
        return redirect('ver_productos')
    
    return render(request, 'producto/agregar_producto.html', {'categorias': categorias})

def ver_productos(request):
    productos = Producto.objects.all().select_related('categoria')
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        producto.categoria_id = request.POST.get('categoria')
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.marca = request.POST.get('marca')
        
        nueva_imagen = request.FILES.get('imagen')
        if nueva_imagen:
            if producto.imagen:
                producto.imagen.delete(save=False)
            producto.imagen = nueva_imagen
            
        producto.save()
        return redirect('ver_productos')
    
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'categorias': categorias
    })

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# VISTAS PARA PEDIDO
def agregar_pedido(request):
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        direccion_envio = request.POST.get('direccion_envio')
        total = request.POST.get('total')
        estado = request.POST.get('estado')
        metodo_pago = request.POST.get('metodo_pago')
        observaciones = request.POST.get('observaciones')
        productos_seleccionados = request.POST.getlist('productos')
        
        pedido = Pedido(
            cliente=cliente,
            direccion_envio=direccion_envio,
            total=total,
            estado=estado,
            metodo_pago=metodo_pago,
            observaciones=observaciones
        )
        pedido.save()
        
        # Agregar productos al pedido (relación muchos a muchos)
        for producto_id in productos_seleccionados:
            producto = Producto.objects.get(id=producto_id)
            pedido.productos.add(producto)
            
        return redirect('ver_pedidos')
    
    return render(request, 'pedido/agregar_pedido.html', {'productos': productos})

def ver_pedidos(request):
    pedidos = Pedido.objects.all().prefetch_related('productos')
    return render(request, 'pedido/ver_pedidos.html', {'pedidos': pedidos})

def actualizar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        pedido.cliente = request.POST.get('cliente')
        pedido.direccion_envio = request.POST.get('direccion_envio')
        pedido.total = request.POST.get('total')
        pedido.estado = request.POST.get('estado')
        pedido.metodo_pago = request.POST.get('metodo_pago')
        pedido.observaciones = request.POST.get('observaciones')
        
        # Actualizar productos del pedido
        productos_seleccionados = request.POST.getlist('productos')
        pedido.productos.clear()
        for producto_id in productos_seleccionados:
            producto = Producto.objects.get(id=producto_id)
            pedido.productos.add(producto)
            
        pedido.save()
        return redirect('ver_pedidos')
    
    return render(request, 'pedido/actualizar_pedido.html', {
        'pedido': pedido,
        'productos': productos
    })

def borrar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})