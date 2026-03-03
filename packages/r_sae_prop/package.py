# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaeProp(RPackage):
	"""Small Area Estimation using Fay-Herriot Models with Additive
Logistic Transformation

	Implements Additive Logistic Transformation (alr) for Small Area Estimation under Fay Herriot Model. Small Area Estimation is used to borrow strength from auxiliary variables to improve the effectiveness of a domain sample size. This package uses Empirical Best Linear Unbiased Prediction (EBLUP). The Additive Logistic Transformation (alr) are based on transformation by Aitchison J (1986). The covariance matrix for multivariate application is based on covariance matrix used by Esteban M, Lombardía M, López-Vizcaíno E, Morales D, and Pérez A <doi:10.1007/s11749-019-00688-w>. The non-sampled models are modified area-level models based on models proposed by Anisa R, Kurnia A, and Indahwati I <doi:10.9790/5728-10121519>, with univariate model using model-3, and multivariate model using model-1. The MSE are estimated using Parametric Bootstrap approach. For non-sampled cases, MSE are estimated using modified approach proposed by Haris F and Ubaidillah A <doi:10.4108/eai.2-8-2019.2290339>.
	"""
	
	homepage = "https://github.com/mrijalussholihin/sae.prop"
	cran = "sae.prop" 

	version("0.1.2", md5="c8de032217ede9439b3a1069a3668029")

	depends_on("r-magic", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
