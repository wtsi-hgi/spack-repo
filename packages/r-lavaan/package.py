# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavaan(RPackage):
	"""Latent Variable Analysis.

	Fit a variety of latent variable models, including confirmatory factor
	analysis, structural equation modeling and latent growth curve models."""

	cran = "lavaan"

	license("GPL-2.0-or-later")

	version("0.6-17", md5="515a33ff0e80effa763913c5e9d641c8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
