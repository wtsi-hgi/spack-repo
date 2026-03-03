# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifehist(RPackage):
	"""Life History Models of Individuals

	Likelihood-based estimation of individual growth and sexual maturity models for organisms, usually fish and invertebrates. It includes methods for data organization, plotting standard exploratory and analytical plots, predictions.
	"""
	
	cran = "LifeHist" 

	version("1.0-1", md5="d4961c187fd6bfdc90d84878084489a2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-optimx@2013.8.6:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
