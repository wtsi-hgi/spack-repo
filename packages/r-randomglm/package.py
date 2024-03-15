# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomglm(RPackage):
	"""Random General Linear Model Prediction.

	The package implements a bagging predictor based on general linear
	models."""

	cran = "randomGLM"

	version("1.10-1", md5="be064b6a4d9d62cd30232c99e3089d99")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
