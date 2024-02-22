# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenmarkov(RPackage):
	"""Multivariate Markov Chains

	Provides routines to estimate the Mixture Transition Distribution Model based on Raftery (1985) <http://www.jstor.org/stable/2345788> and Nicolau (2014) <doi:10.1111/sjos.12087> specifications, for multivariate data. Additionally, provides a  function for the estimation of a new model for multivariate non-homogeneous Markov chains. This new specification, Generalized Multivariate Markov Chains (GMMC) was proposed by Carolina Vasconcelos and Bruno Damasio and considers (continuous or discrete) covariates exogenous to the Markov chain.
	"""
	
	cran = "GenMarkov" 

	version("0.2.0", md5="bd69f0a76ed8fd8e139366d81297dd5a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-alabama@2015.3.1:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-hmisc@4.5.0:", type=("build", "run"))
	depends_on("r-matrixcalc@1.0.3:", type=("build", "run"))
	depends_on("r-maxlik@1.4.8:", type=("build", "run"))
	depends_on("r-nnet@7.3.16:", type=("build", "run"))
