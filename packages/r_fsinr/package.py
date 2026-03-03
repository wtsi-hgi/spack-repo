# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsinr(RPackage):
	"""Feature Selection

	Feature subset selection algorithms modularized in search algorithms and measure utilities. Full list and more information available at <https://dicits.ugr.es/software/FSinR/>.
	"""
	
	cran = "FSinR" 

	version("2.0.5", md5="d2c79ef371ffa8aa9345abcba4f8d6a0")

	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
