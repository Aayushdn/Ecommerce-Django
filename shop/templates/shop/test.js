<script>
    if (localStorage.getItem('cart') == null) {
        var cart = {};
    }
    else {
        cart = JSON.parse(localStorage.getItem('cart'));
        updateCart(cart);
        
    }
    $('.divpr').on("click","button.cart",function () {
        console.log('clicked');
        var idstr = this.id.toString();
        console.log(idstr);
        if (cart[idstr] != undefined) {
            cart[idstr][0] = cart[idstr][0] + 1;
        }
        else {
            qty = 1
            name_prd = document.getElementById('name' + idstr).innerHTML;
            cart[idstr] = [qty , name_prd];
        }
        
        
        console.log(cart);
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCart(cart);
    });
    updatePopover(cart)

    document.getElementById("popcart").setAttribute('data-content', '<h5>Cart for your items in my shopping cart</h5>'); 
    function updateCart(cart){
        var sum = 0
        for (var item in cart){
            sum = sum + cart[item][0]
            document.getElementById('div' + item).innerHTML = ("<button class='btn btn-primary minus' id='minus" +  item + "'>  - </button> <span id='val" + item + "'>" + cart[item][0] + "</span> <button class='btn btn-primary plus' id='plus" + item + "'> + </button>");
            updatePopover(cart)

        }
        updatePopover(cart)
        document.getElementById('cart').innerHTML = sum;
    }
    
    
    function updatePopover(cart){
        popStr = '<h5> Cart for your items in my shopping cart </h5> <br> <div classs="container">'
        popStr =  popStr + '<div class = "row"><div class="col-md-12"><b>Items</b>' + '<b><p style= "float:right;">Qty:</p></b></div></div>'
        for (var item in cart){
            popStr = popStr + '<br> '
            popStr = popStr + '<div class="row"> <div class="col-md-12"> ' +  document.getElementById('name' +  item).innerHTML  +  '<p style= "float:right;">' + cart[item][0] + '</p> <hr></div> </div>';
            

        }
        popStr = popStr + '<div class="bottomNav"><a href="/shop/checkout"><button class="btn btn-primary" id="checkout">Proced to Pay</button></a> <button class="btn btn-primary" id="ClearCart" onclick="clearCart()">Clear Cart</button></div>'
        popStr = popStr + '</div>' 
        document.getElementById('popcart').setAttribute('data-content',popStr)
        $('#popcart').popover('show');

    }

    $('.divpr').on('click' , 'button.minus' , function(){
        a = this.id.slice(5,);
        cart[a][0] = cart[a][0] - 1;
        cart[a][0] = Math.max(0,cart[a][0])
        document.getElementById('val' + a).innerHTML = cart[a][0]
        updateCart(cart)
        

    });

    $('.divpr').on('click' , 'button.plus' , function(){
        a = this.id.slice(4,);
        cart[a][0] = cart[a][0] + 1;
        document.getElementById('val' + a).innerHTML = cart[a][0]
        updateCart(cart)

    });

    function clearCart(){
        cart = JSON.parse(localStorage.getItem('cart'));
        for (var item in cart){
            document.getElementById('div'+ item).innerHTML = document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-primary cart">Add To Cart</button>'
        }

        localStorage.clear()
        cart={}
        updateCart(cart)
    }






</script>