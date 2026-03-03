# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenscore(RPackage):
	"""Generalized Score Matching Estimators

	Implementation of the Generalized Score Matching estimator in Yu et al. (2019) <https://jmlr.org/papers/v20/18-278.html> for non-negative graphical models (truncated Gaussian, exponential square-root, gamma, a-b models) and univariate truncated Gaussian distributions. Also includes the original estimator for untruncated Gaussian graphical models from Lin et al. (2016) <doi:10.1214/16-EJS1126>, with the addition of a diagonal multiplier.
	"""
	
	homepage = "https://github.com/sqyu/genscore"
	cran = "genscore" 

	version("1.0.2.2", md5="17e067b57e72ab4cd57c01af5ba8bc15")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
