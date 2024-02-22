# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpm(RPackage):
	"""Sequential and Batch Change Detection Using Parametric and
Nonparametric Methods

	Sequential and batch change detection for univariate data streams, using the change point model framework. Functions are provided to allow nonparametric distribution-free change detection in the mean, variance, or general distribution of a given sequence of observations. Parametric change detection methods are also provided for Gaussian, Bernoulli and Exponential sequences. Both the batch (Phase I) and sequential (Phase II) settings are supported, and the sequences may contain either a single or multiple change points. A full description of this package is available in Ross, G.J (2015) - "Parametric and nonparametric sequential change detection in R" available at <https://www.jstatsoft.org/article/view/v066i03>.
	"""
	
	cran = "cpm" 

	version("2.3", md5="a971f69747b7afcb44992f80faba591b")

	depends_on("r@2.15:", type=("build", "run"))
