# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychomix(RPackage):
	"""Psychometric Mixture Models

	Psychometric mixture models based on 'flexmix' infrastructure. At the moment Rasch mixture models
  with different parameterizations of the score distribution (saturated vs. mean/variance specification),
  Bradley-Terry mixture models, and MPT mixture models are implemented. These mixture models can be estimated
  with or without concomitant variables. See vignette('raschmix', package = 'psychomix') for details on the
  Rasch mixture models.
	"""
	
	cran = "psychomix" 

	version("1.1-8", md5="3e1759600a292803ca1b8f1a8c0dd8ef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-flexmix@2.3.7:", type=("build", "run"))
	depends_on("r-psychotools@0.4.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-formula@1.1.0:", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
