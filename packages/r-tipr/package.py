# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTipr(RPackage):
	"""Tipping Point Analyses

	The strength of evidence provided by epidemiological and
    observational studies is inherently limited by the potential for
    unmeasured confounding.  We focus on three key quantities: the
    observed bound of the confidence interval closest to the null, the
    relationship between an unmeasured confounder and the outcome, for
    example a plausible residual effect size for an unmeasured continuous
    or binary confounder, and the relationship between an unmeasured
    confounder and the exposure, for example a realistic mean difference
    or prevalence difference for this hypothetical confounder between
    exposure groups. Building on the methods put forth by Cornfield et al.
    (1959), Bross (1966), Schlesselman (1978), Rosenbaum & Rubin (1983),
    Lin et al. (1998), Lash et al. (2009), Rosenbaum (1986), Cinelli &
    Hazlett (2020), VanderWeele & Ding (2017), and Ding & VanderWeele
    (2016), we can use these quantities to assess how an unmeasured
    confounder may tip our result to insignificance.
	"""
	
	homepage = "https://r-causal.github.io/tipr/"
	cran = "tipr" 

	version("1.0.2", md5="4fa9bdead445e96c1c52b9f8038a1dbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli@3.4.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-sensemakr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
