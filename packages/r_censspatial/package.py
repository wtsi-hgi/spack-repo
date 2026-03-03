# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensspatial(RPackage):
	"""Censored Spatial Models

	It fits linear regression models for censored spatial data. It provides different estimation methods as the SAEM (Stochastic Approximation of Expectation Maximization) algorithm and seminaive that uses Kriging prediction to estimate the response at censored locations and predict new values at unknown locations. It also offers graphical tools for assessing the fitted model. More details can be found in Ordonez et al. (2018) <doi:10.1016/j.spasta.2017.12.001>.
	"""
	
	cran = "CensSpatial" 

	version("3.6", md5="f25723c38e519e1ee7f07a06d4d58eee")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-geor@1.8.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-optimx@2021.10.12:", type=("build", "run"))
	depends_on("r-tmvtnorm@1.4.10:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-numderiv@2.11.1:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-tlrmvnmvt@1.1:", type=("build", "run"))
