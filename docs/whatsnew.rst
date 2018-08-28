What’s New in Boundless Exchange v1.4.11
=========================================

Welcome to the latest update of Boundless Exchange! This release includes OAuth authentication improvements, bounding box updates in MapLoom, and numerous bug fixes.

Authentication
^^^^^^^^^^^^^^

Boundless Exchange uses OAuth to grant users and applications access to shared information, without giving access to the passwords. This release provides the following changes:

 * It is now possible for Boundless Anywhere to use the configured GeoAxis or Auth0 authentication provider in Exchange for secure token exchange and validation.

 * Support for Auth0 OpenID Connect (OIDC) conformity.
 
 * Federated logout of third-party authentication providers.

MapLoom
^^^^^^^^^^^^^^^^

 * Layer bounding boxes are now automatically recalculated when editing vector features in MapLoom.