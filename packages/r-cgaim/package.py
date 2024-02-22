# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgaim(RPackage):
	"""Constrained Groupwise Additive Index Models

	Fits constrained groupwise additive index models and provides functions for inference and interpretation of these models. The method is described in Masselot, Chebana, Campagna, Lavigne, Ouarda, Gosselin (2022) "Constrained groupwise additive index models" <doi:10.1093/biostatistics/kxac023>.
	"""
	
	cran = "cgaim" 

	version("1.0.0", md5="f8b20791fdfb88540266be7977eafe16")

	depends_on("r-scam", type=("build", "run"))
	depends_on("r-scar", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cgam", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gratia", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-coneproj", type=("build", "run"))
	depends_on("r-truncatednormal", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
