# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchmix(RPackage):
	"""Semi-Supervised Bayesian Mixture Models Incorporating Batch
Correction

	Semi-supervised and unsupervised Bayesian mixture models that
  simultaneously infer the cluster/class structure and a batch correction.
  Densities available are the multivariate normal and the multivariate t.
  The model sampler is implemented in C++. This package is aimed at analysis of
  low-dimensional data generated across several batches. See Coleman et al.
  (2022) <doi:10.1101/2022.01.14.476352> for details of the model.
	"""
	
	homepage = "https://github.com/stcolema/batchmix"
	cran = "batchmix" 

	version("2.1.0", md5="9191b5c5d1c34ed9b22a34b887e2968a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
