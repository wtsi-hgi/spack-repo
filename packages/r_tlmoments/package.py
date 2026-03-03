# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlmoments(RPackage):
	"""Calculate TL-Moments and Convert Them to Distribution Parameters

	Calculates empirical TL-moments (trimmed L-moments) of arbitrary 
    order and trimming, and converts them to distribution parameters. 
	"""
	
	cran = "TLMoments" 

	version("0.7.5.3", md5="d5d5a6e4d8377a998bc6fc9d7f860b2c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
