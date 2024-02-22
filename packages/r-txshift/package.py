# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxshift(RPackage):
	"""Efficient Estimation of the Causal Effects of Stochastic
Interventions

	Efficient estimation of the population-level causal effects of
    stochastic interventions on a continuous-valued exposure. Both one-step and
    targeted minimum loss estimators are implemented for the counterfactual mean
    value of an outcome of interest under an additive modified treatment policy,
    a stochastic intervention that may depend on the natural value of the
    exposure. To accommodate settings with outcome-dependent two-phase
    sampling, procedures incorporating inverse probability of censoring
    weighting are provided to facilitate the construction of inefficient and
    efficient one-step and targeted minimum loss estimators.  The causal
    parameter and its estimation were first described by Díaz and van der Laan
    (2013) <doi:10.1111/j.1541-0420.2011.01685.x>, while the multiply robust
    estimation procedure and its application to data from two-phase sampling
    designs is detailed in NS Hejazi, MJ van der Laan, HE Janes, PB Gilbert,
    and DC Benkeser (2020) <doi:10.1111/biom.13375>. The software package
    implementation is described in NS Hejazi and DC Benkeser (2020)
    <doi:10.21105/joss.02447>. Estimation of nuisance parameters may be
    enhanced through the Super Learner ensemble model in 'sl3', available for
    download from GitHub using 'remotes::install_github("tlverse/sl3")'.
	"""
	
	homepage = "https://github.com/nhejazi/txshift"
	cran = "txshift" 

	version("0.3.8", md5="99f3214a842cbe9b85cdc8676e6f13d1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-hal9001@0.4.1:", type=("build", "run"))
	depends_on("r-haldensify@0.2.1:", type=("build", "run"))
	depends_on("r-lspline", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
