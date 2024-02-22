# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemist(RPackage):
	"""Causal Inference with High-Dimensional Error-Prone Covariates
and Misclassified Treatments

	
    We aim to deal with the average treatment effect (ATE), where the data are
    subject to high-dimensionality and measurement error. This package primarily contains two 
    functions, which are used to generate artificial data and estimate ATE with high-dimensional 
    and error-prone data accommodated.
	"""
	
	cran = "CHEMIST" 

	version("0.1.5", md5="cb6c4f225aea61cce7f5e59442a42f4b")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-xicor", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
