# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdta(RPackage):
	"""Data Transforming Augmentation for Linear Mixed Models

	We provide a toolbox to fit univariate and multivariate linear mixed models via data transforming augmentation. Users can also fit these models via typical data augmentation for a comparison. It returns either maximum likelihood estimates of unknown model parameters (hyper-parameters) via an EM algorithm or posterior samples of those parameters via MCMC. Also see Tak et al. (2019) <doi:10.1080/10618600.2019.1704295>.
	"""
	
	cran = "Rdta" 

	version("1.0.1", md5="90959e76e94c2de4e98ee569a64373f4")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-mcmcpack@1.4.4:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.11:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
