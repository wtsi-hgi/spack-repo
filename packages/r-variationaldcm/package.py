# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariationaldcm(RPackage):
	"""Variational Bayesian Estimation for Diagnostic Classification
Models

	Enables computationally efficient parameters-estimation by variational Bayesian methods for various diagnostic classification models (DCMs). DCMs are a class of discrete latent variable models for classifying respondents into latent classes that typically represent distinct combinations of skills they possess. Recently, to meet the growing need of large-scale diagnostic measurement in the field of educational, psychological, and psychiatric measurements, variational Bayesian inference has been developed as a computationally efficient alternative to the Markov chain Monte Carlo methods, e.g., Yamaguchi and Okada (2020a) <doi:10.1007/s11336-020-09739-w>, Yamaguchi and Okada (2020b) <doi:10.3102/1076998620911934>, Yamaguchi (2020) <doi:10.1007/s41237-020-00104-w>, Oka and Okada (2023) <doi:10.1007/s11336-022-09884-4>, and Yamaguchi and Martinez (2023) <doi:10.1111/bmsp.12308>. To facilitate their applications, 'variationalDCM' is developed to provide a collection of recently-proposed variational Bayesian estimation methods for various DCMs.
	"""
	
	homepage = "https://github.com/khijikata/variationalDCM"
	cran = "variationalDCM" 

	version("2.0.1", md5="84d386dfbfc8834bef5689787e122876")
	version("1.0.0", md5="2149ded9a1088a5c84a2570e757e1b40")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
