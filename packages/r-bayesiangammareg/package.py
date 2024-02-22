# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesiangammareg(RPackage):
	"""Bayesian Gamma Regression: Joint Mean and Shape Modeling

	Adjust the Gamma regression models from a Bayesian perspective described by Cepeda and Urdinola (2012) <doi:10.1080/03610918.2011.600500>, modeling the parameters of mean and shape and using different link functions for the parameter associated to the mean. And calculates different adjustment statistics such as the Akaike information criterion and Bayesian information criterion.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "Bayesiangammareg" 

	version("0.1.0", md5="cb076b71dc2d9b58e299a03605e998c3")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
