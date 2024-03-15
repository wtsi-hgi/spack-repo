# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnet(RPackage):
	"""Feed-Forward Neural Networks and Multinomial Log-Linear Models.

	Software for feed-forward neural networks with a single hidden layer, and
	for multinomial log-linear models."""

	cran = "nnet"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("7.3-19", md5="70c6d1ad4a564b28373ffc7b7edd28d1")

	depends_on("r@3:", type=("build", "run"))
