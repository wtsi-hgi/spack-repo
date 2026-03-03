# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdp(RPackage):
	"""Implementation of the Bayesian Discount Prior Approach for
Clinical Trials

	Functions for data augmentation using the Bayesian discount prior 
    method for single arm and two-arm clinical trials, as described in Haddad 
    et al. (2017) <doi:10.1080/10543406.2017.1300907>. The discount power prior 
    methodology was developed in collaboration with the The Medical Device 
    Innovation Consortium (MDIC) Computer Modeling & Simulation Working Group.
	"""
	
	homepage = "https://github.com/graemeleehickey/bayesDP"
	cran = "bayesDP" 

	version("1.3.6", md5="c7ec5f136c65e565b9057c339b8337a9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
