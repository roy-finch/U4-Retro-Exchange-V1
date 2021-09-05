/*
    This is to create and enable the stripe smart checkout.
    Used https://stripe.com.docs/payments/accept-a-payment
    to create functionality of the payment methods.
*/

var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
var client_key = $("#id_client_key").text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        fontFamily: '"Segoe UI", sans-serif',
    },
    invalid: {
        color: "red",
    }
};

var card = elements.create("card");
card.mount("#card-element", {style: style});

card.addEventListener("change", function(event) {
    var errorC = document.getElementById("card-errors");
    if (event.error) {
        var html =
            <span class="error">${ event.error.message }</span>
        $(errorC).html(html)
    } else {
        errorC.textContent = '';
    }
});