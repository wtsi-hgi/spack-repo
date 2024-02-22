# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcirt(RPackage):
	"""IRT Models for Polytomous and Continuous Item Responses

	Estimates the multidimensional polytomous Rasch model (Rasch, 1961) with conditional maximum likelihood estimation.
	"""
	
	homepage = "https://github.com/christinehohensinn/pcIRT"
	cran = "pcIRT" 

	version("0.2.4", md5="ea035ed0648d32b7011a7407119530a9")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
