# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrnn(RPackage):
	"""Bayesian Regularization for Feed-Forward Neural Networks

	Bayesian regularization for feed-forward neural networks.
	"""
	
	cran = "brnn" 

	version("0.9.3", md5="be5013b63fdfd8415c1e9f8d74b34397")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
