# Stripe Payment Link redirect configuration

This report identifies the current checkout CTA destination(s) in the deployed `origin/main` source. It is a configuration handoff only; no Stripe configuration or Payment Link was changed.

## Discovered checkout CTA mapping

| Product | Source controls | Existing Stripe Payment Link | Existing identifier | Required post-payment redirect URL |
|---|---|---|---|---|
| Jugendamt Antwort | `index.html`: navigation, hero, final section, mobile sticky CTA | `https://buy.stripe.com/6oUcN78cs3jr8Hy8iZ8og0b` | `6oUcN78cs3jr8Hy8iZ8og0b` | `https://website.rebellsystem.com/success.html?session_id={CHECKOUT_SESSION_ID}` |

## Stripe dashboard steps — perform separately for this link

1. Open Payment Links and select the link ending in `6oUcN78cs3jr8Hy8iZ8og0b`.
2. In the link's post-payment settings, choose **Redirect to a URL** (not Stripe's hosted confirmation page).
3. Set the redirect URL exactly to `https://website.rebellsystem.com/success.html?session_id={CHECKOUT_SESSION_ID}`.
4. Save the link. Do not change the product, price, checkout copy, or the Payment Link URL.

`{CHECKOUT_SESSION_ID}` is replaced by Stripe after a completed Checkout Session. The static success page emits `purchase` only when that parameter is present and matches a Stripe Checkout Session ID shape; a generic visit emits no purchase event. The page intentionally does not claim a price, product, or payment status it cannot verify without a server-side Stripe integration.
