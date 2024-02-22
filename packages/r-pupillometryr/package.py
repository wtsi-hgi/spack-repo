# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPupillometryr(RPackage):
	"""A Unified Pipeline for Pupillometry Data

	Provides a unified pipeline to clean, prepare, plot,
    and run basic analyses on pupillometry experiments.
	"""
	
	cran = "PupillometryR" 

	version("0.0.5", md5="cbe47676be321d31d250aba7d301d79d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-itsadug", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
