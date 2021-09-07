/*
    This is to create and enable the stripe smart checkout.
    Used https://stripe.com/docs/payments/accept-a-payment
    to create functionality of the payment methods.
*/

var stripePublicKey = document.getElementById("id_stripe_public_key").getAttribute("content");
var clientKey = document.getElementById("id_client_key").getAttribute("content");
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        fontFamily: '"Segoe UI", sans-serif',
        color: "blue",
    },
    invalid: {
        color: "red",
    }
};

var card = elements.create("card", {
    style: style
});
card.mount("#card-element");

card.addEventListener("change", function(event) {
    var errorC = document.getElementById("card-errors");
    if (event.error) {
        var html = `
        <span> ${ event.error.message } </span>
        `;
        errorC.innerHTML = html;
    } else {
        errorC.innerHTML = "";
    }
});

var form = document.querySelector("payment-form");

form.addEventListener("submit", function(ev) {
    ev.preventDefault();
    card.update({
        "disabled": true
    });
    document.getElementById("submit").setAttribute("disabled", true);
    stripe.confirmCardPayment(clientKey, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var html = "<span class='error'>${ event.error.message }</span>";
            $(errorC).html(html);
            card.update({
                "disabled": false
            });
            document.getElementById("submit").setAttribute("disabled", false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    })
})