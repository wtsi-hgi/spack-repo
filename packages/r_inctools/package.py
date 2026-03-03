# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInctools(RPackage):
	"""Incidence Estimation Tools

	Tools for estimating incidence from biomarker data in cross-
    sectional surveys, and for calibrating tests for recent infection. 
    Implements and extends the method of Kassanjee et al. (2012)
    <doi:10.1097/EDE.0b013e3182576c07>.
	"""
	
	homepage = "http://www.incidence-estimation.org/page/inctools"
	cran = "inctools" 

	version("1.0.15", md5="0859f4a2cff48e59f668e44eca1c7b68")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
