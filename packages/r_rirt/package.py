# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRirt(RPackage):
	"""Data Analysis and Parameter Estimation Using Item Response
Theory

	Parameter estimation, computation of probability, information, and 
    (log-)likelihood, and visualization of item/test characteristic curves and
    item/test information functions for three uni-dimensional item response theory
    models: the 3-parameter-logistic model, generalized partial credit model, 
    and graded response model. The full documentation and tutorials are at 
    <https://github.com/xluo11/Rirt>.
	"""
	
	homepage = "https://github.com/xluo11/Rirt"
	cran = "Rirt" 

	version("0.0.2", md5="906ea351394a899a129011faaabd6a52")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
