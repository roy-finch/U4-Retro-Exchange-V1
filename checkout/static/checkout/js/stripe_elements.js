/*
    This is to create and enable the stripe smart checkout.
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
        color: 'red',
    }
};

var card = elements.create("card", {style: style});
card.mount("#card-div");