# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeedglm(RPackage):
	"""Fitting Linear and Generalized Linear Models to Large Data Sets.

	Fitting linear models and generalized linear models to large data sets by
	updating algorithms."""

	cran = "speedglm"

	license("GPL-2.0-or-later")

	version("0.3-5", md5="48a7f9d2722b0142fc0372a6d8769acf")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-biglm", type=("build", "run"))
