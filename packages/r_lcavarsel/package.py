# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcavarsel(RPackage):
	"""Variable Selection for Latent Class Analysis

	Variable selection for latent class analysis for model-based clustering of multivariate categorical data. The package implements a general framework for selecting the subset of variables with relevant clustering information and discard those that are redundant and/or not informative. The variable selection method is based on the approach of Fop et al. (2017) <doi:10.1214/17-AOAS1061> and Dean and Raftery (2010) <doi:10.1007/s10463-009-0258-9>. Different algorithms are available to perform the selection: stepwise, swap-stepwise and evolutionary stochastic search. Concomitant covariates used to predict the class membership probabilities can also be included in the latent class analysis model. The selection procedure can be run in parallel on multiple cores machines.
	"""
	
	homepage = "https://michaelfop.github.io/"
	cran = "LCAvarsel" 

	version("1.1", md5="d5fd37a54b6526ebaea630372d56faf8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-polca@1.4.1:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
