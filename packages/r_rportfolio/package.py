# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRportfolio(RPackage):
	"""Portfolio Theory

	Collection of tools to calculate portfolio performance metrics. Portfolio performance is a key measure for investors. These metrics are important to analyse how effectively their money has been invested. This package uses portfolio theories to give investor tools to evaluate their portfolio performance. For more information see,  Markowitz, H.M. (1952), <doi:10.2307/2975974>. Analysis of Investments & Management of Portfolios [2012, ISBN:978-8131518748]. 
	"""
	
	cran = "rportfolio" 

	version("0.0.3", md5="96895949f231d50f0c9c5e6079fe9956")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
