# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisclassglm(RPackage):
	"""Computation of Generalized Linear Models with Misclassified
Covariates Using Side Information

	Estimates models that extend the standard GLM to take
    misclassification into account. The models require side information from a secondary data set
    on the misclassification process, i.e. some sort of misclassification
    probabilities conditional on some common covariates.
    A detailed description of the algorithm can be found in
    Dlugosz, Mammen and Wilke (2015) <https://www.zew.de/publikationen/generalised-partially-linear-regression-with-misclassified-data-and-an-application-to-labour-market-transitions>.
	"""
	
	cran = "misclassGLM" 

	version("0.3.5", md5="39f77b4d105741d3912bc5c38bba2a78")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
