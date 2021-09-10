/*
    This is to create and enable the stripe smart checkout.
    Used https://stripe.com/docs/payments/accept-a-payment
    to create functionality of the payment methods.

    This file sets up the payments and transactions of my site
    it uses stripe features to create and take payments.
*/
var stripePublicKey = document.getElementById("id_stripe_public_key").getAttribute("content").slice(1, -1);
var clientKey = document.getElementById("id_client_key").getAttribute("content").slice(1, -1);
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

var form = document.getElementById("payment-form");

form.addEventListener("submit", function(ev) {
    ev.preventDefault();
    card.update({
        "disabled": true
    });
    document.getElementById("submit").setAttribute("disabled", true);
    var saveOrder = Boolean($("#id-save-order").attr("checked"));
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    var postData = {
        "csrfmiddlewaretoken": csrfToken,
        "client_key": clientKey,
        "save_order": saveOrder,
    };
    var url = "/checkout/cache_checkout_data/";

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientKey, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        country: $.trim(form.country.value),
                        county: $.trim(form.county.value),
                        city: $.trim(form.town_r_city.value),
                        line1: $.trim(form.street_add_line1.value),
                        line2: $.trim(form.street_add_line2.value),
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        country: $.trim(form.country.value),
                        county: $.trim(form.county.value),
                        city: $.trim(form.town_r_city.value),
                        line1: $.trim(form.street_add_line1.value),
                        line2: $.trim(form.street_add_line2.value),
                        post_code: $.trim(form.post_code.value),
                    }
                }
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
    }).fail(function () {
        location.reload();
    })
})