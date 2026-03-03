# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesplay(RPackage):
	"""The Bayes Factor Playground

	A lightweight modelling syntax for defining likelihoods and priors
    and for computing Bayes factors for simple one parameter models. It includes
    functionality for computing and plotting priors, likelihoods, and model
    predictions. Additional functionality is included for computing and plotting
    posteriors.
	"""
	
	homepage = "https://github.com/bayesplay/bayesplay"
	cran = "bayesplay" 

	version("0.9.3", md5="94719d700b4c31786ba212e61eaf479d")

	depends_on("r-gginnards", type=("build", "run"))
