# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabapplstat(RPackage):
	"""Miscellaneous Scripts from the Data Science Laboratory (UCPH)

	Miscellaneous scripts, e.g. functionality to make and plot factor diagrams for the statistical design.
	"""
	
	cran = "LabApplStat" 

	version("1.4.4", md5="e1afbd74101651c069382bd271670e59")

	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
