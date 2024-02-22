# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomizer(RPackage):
	"""Randomization for Clinical Trials

	This tool enables the user to choose a randomization procedure
    based on sound scientific criteria. It comprises the generation of
    randomization sequences as well the assessment of randomization procedures
    based on carefully selected criteria. Furthermore, 'randomizeR' provides a
    function for the comparison of randomization procedures.
	"""
	
	cran = "randomizeR" 

	version("3.0.2", md5="f33332b1708a82cfb15913e01803ed3f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mstate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-pwrgsd", type=("build", "run"))
	depends_on("r-gsdesign", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
