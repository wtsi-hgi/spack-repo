# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgdinference(RPackage):
	"""Inference with Stochastic Gradient Descent

	Estimation and inference methods for large-scale mean and quantile regression models via stochastic (sub-)gradient descent (S-subGD) algorithms. 
    The inference procedure handles cross-sectional data sequentially: 
    (i) updating the parameter estimate with each incoming "new observation", 
    (ii) aggregating it as a Polyak-Ruppert average, and 
    (iii) computing an asymptotically pivotal statistic for inference through random scaling. 
    The methodology used in the 'SGDinference' package is described in detail in the following papers: 
    (i) Lee, S., Liao, Y., Seo, M.H. and Shin, Y. (2022) <doi:10.1609/aaai.v36i7.20701> "Fast and robust online inference with stochastic gradient descent via random scaling".
    (ii) Lee, S., Liao, Y., Seo, M.H. and Shin, Y. (2023) <arXiv:2209.14502> "Fast Inference for Quantile Regression with Tens of Millions of Observations". 
	"""
	
	homepage = "https://github.com/SGDinference-Lab/SGDinference/"
	cran = "SGDinference" 

	version("0.1.0", md5="261d52b8402c0bea0b3d0b2c6c461f77")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
