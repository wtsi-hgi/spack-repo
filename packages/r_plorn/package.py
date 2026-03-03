# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlorn(RPackage):
	"""Prediction with Less Overfitting and Robust to Noise

	A method for the quantitative prediction with much predictors. 
    This package provides functions to construct the quantitative prediction 
    model with less overfitting and robust to noise. 
	"""
	
	homepage = "https://github.com/takakoizumi/PLORN"
	cran = "PLORN" 

	version("0.1.1", md5="066421e4c7ca3869fad1df43d98787ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
