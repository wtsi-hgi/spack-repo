# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrailtypack(RPackage):
    """Shared, Joint (Generalized) Frailty Models; Surrogate Endpoints

        The following several classes of frailty models using a penalized likelihood estimation on the hazard function but also a parametric estimation can be fit using this R package:
        1) A shared frailty model (with gamma or log-normal frailty distribution) and Cox proportional hazard model. Clustered and recurrent survival times can be studied.
        2) Additive frailty models for proportional hazard models with two correlated random effects (intercept random effect with random slope).
        3) Nested frailty models for hierarchically clustered data (with 2 levels of clustering) by including two iid gamma random effects.
        4) Joint frailty models in the context of the joint modelling for recurrent events with terminal event for clustered data or not. A joint frailty model for two semi-competing risks and clustered data is also proposed.
                5) Joint general frailty models in the context of the joint modelling for recurrent events with terminal event data with two independent frailty terms.
                6) Joint Nested frailty models in the context of the joint modelling for recurrent events with terminal event, for hierarchically clustered data (with two levels of clustering) by including two iid gamma random effects.
                7) Multivariate joint frailty models for two types of recurrent events and a terminal event.
                8) Joint models for longitudinal data and a terminal event.
                9) Trivariate joint models for longitudinal data, recurrent events and a terminal event.
                10) Joint frailty models for the validation of surrogate endpoints in multiple randomized clinical trials with failure-time and/or longitudinal endpoints
                with the possibility to use a mediation analysis model.
    11) Conditional and Marginal two-part joint models for longitudinal semicontinuous data and a terminal event.
    12) Joint frailty-copula models for the validation of surrogate endpoints in multiple randomized clinical trials with failure-time endpoints.
                13) Generalized shared and joint frailty models for recurrent and terminal events. Proportional hazards (PH), additive hazard (AH), proportional odds (PO) and probit models are available in a fully parametric framework. For PH and AH models, it is possible to consider type-varying coefficients and flexible semiparametric hazard function.
                Prediction values are available (for a terminal event or for a new recurrent event). Left-truncated (not for Joint model), right-censored data, interval-censored data (only for Cox proportional hazard and shared frailty model) and strata are allowed. In each model, the random effects have the gamma or normal distribution. Now, you can also consider time-varying covariates effects in Cox, shared and joint frailty models (1-5). The package includes concordance measures for Cox proportional hazards models and for shared frailty models.
    14) Competing Joint Frailty Model: A single type of recurrent event and two terminal events.
    Moreover, the package can be used with its shiny application, in a local mode or by following the link below.
    """

    homepage = "https://virginie1rondeau.wixsite.com/virginierondeau/software-frailtypack"
    cran = "frailtypack"

    version("3.6.0", md5="cdb42ba05529fb9a190133f014c836d7")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-survc1", type=("build", "run"))
    depends_on("r-doby", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
    depends_on("r-nlme", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-rootsolve", type=("build", "run"))

    def setup_build_environment(self, env):
        env.set("MAKEFLAGS", "-j1")
