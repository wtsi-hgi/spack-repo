# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianlaterality(RPackage):
	"""Predict Brain Asymmetry Based on Handedness and Dichotic
Listening

	Functional differences between the cerebral hemispheres 
    are a fundamental characteristic of the human brain. Researchers 
    interested in studying these differences often infer underlying 
    hemispheric dominance for a certain function (e.g., language) from 
    laterality indices calculated from observed performance or brain 
    activation measures . However, any inference from observed measures 
    to latent (unobserved) classes has to consider the prior probability 
    of class membership in the population. The provided functions 
    implement a Bayesian model for predicting hemispheric dominance from
    observed laterality indices (Sorensen and Westerhausen, Laterality: 
    Asymmetries of Body, Brain and Cognition, 2020, <doi:10.1080/1357650X.2020.1769124>).
	"""
	
	homepage = "https://github.com/LCBC-UiO/BayesianLaterality"
	cran = "BayesianLaterality" 

	version("0.1.2", md5="79950d899465ca18c494baf3b682f9f3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-tmvtnorm@1.4.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
