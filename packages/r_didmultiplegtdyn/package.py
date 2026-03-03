# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDidmultiplegtdyn(RPackage):
	"""Estimation in Difference-in-Difference Designs with Multiple
Groups and Periods

	Estimation of event-study Difference-in-Difference (DID) estimators in designs with multiple groups and periods, and with a potentially non-binary treatment that may increase or decrease multiple times. 
	"""
	
	cran = "DIDmultiplegtDYN" 

	version("1.0.5", md5="0ba47f49e38541d397b3b7065f7ed99b")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matlib", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
