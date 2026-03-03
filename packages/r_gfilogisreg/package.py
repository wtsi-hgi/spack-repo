# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfilogisreg(RPackage):
	"""Generalized Fiducial Inference for Binary Logistic Regression
Models

	Fiducial framework for the logistic regression model. The fiducial distribution of the parameters of the logistic regression is simulated, allowing to perform statistical inference on any parameter of interest. The algorithm is taken from Jessi Cisewski's PhD thesis: Jessi Cisewski (2012), "Generalized fiducial inference for mixed linear models".
	"""
	
	cran = "gfilogisreg" 

	version("1.0.3", md5="e7ac5ed8f951b8f059c1a9fcfbfa2fd4")

	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-spatstat@2:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-eigenr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
