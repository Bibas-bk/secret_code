// Simple Cart Logic
let cartCount = 0;
const cartCountElement = document.getElementById('cart-count');

function addToCart() {
    cartCount++;
    cartCountElement.innerText = cartCount;
    
    // Optional: Visual feedback
    alert("Item added to cart!");
}

function toggleCart() {
    if(cartCount === 0) {
        alert("Your cart is empty!");
    } else {
        alert(`You have ${cartCount} items in your cart. Proceed to checkout.`);
    }
}