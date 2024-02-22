# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsd(RPackage):
	"""Graphical Shim for Visual Survival Data Analysis

	Provides a shim command for survival analysis graphic generation.
	"""
	
	cran = "vsd" 

	version("0.1.0", md5="449a8f82d93fd6ae3717fce038541e80")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-muhaz", type=("build", "run"))
