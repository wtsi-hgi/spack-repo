# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBglr(RPackage):
	"""Bayesian Generalized Linear Regression."""

	cran = "BGLR"

	version("1.1.1", md5="3d50bee4573929251d2fab3fd841c973")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
