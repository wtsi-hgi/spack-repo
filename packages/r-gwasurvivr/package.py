# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasurvivr(RPackage):
	"""gwasurvivr: an R package for genome wide survival analysis

	gwasurvivr is a package to perform survival analysis using Cox proportional hazard models on imputed genetic data.
	"""
	
	homepage = "https://github.com/suchestoncampbelllab/gwasurvivr"
	bioc = "gwasurvivr"

	version("1.26.0", commit="5478a68a557d4ecc47ee9564b63f1900db34aa62")
	version("1.20.0", commit="34fb4cb8db6edaab5c99a3fd8d66406bb6918c53")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gwastools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
