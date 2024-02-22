# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptgauss(RPackage):
	"""Gaussian Mixture Models (GMM)

	Multimodal distributions can be modelled as a mixture of components. The model is derived using the Pareto Density Estimation (PDE) for an estimation of the pdf. PDE has been designed in particular to identify groups/classes in a dataset. Precise limits for the classes can be calculated using the theorem of Bayes. Verification of the model is possible by QQ plot, Chi-squared test and Kolmogorov-Smirnov test. The package is based on the publication of Ultsch, A., Thrun, M.C., Hansen-Goos, O., Lotsch, J. (2015)  <DOI:10.3390/ijms161025897>.
	"""
	
	homepage = "https://www.deepbionics.org"
	cran = "AdaptGauss" 

	version("1.6", md5="54c3fc08f481c0cd2a09a937918c6bf4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-datavisualizations", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
