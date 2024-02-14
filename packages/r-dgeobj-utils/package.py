# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgeobjUtils(RPackage):
	"""Differential Gene Expression (DGE) Analysis Utility Toolkit

	
    Provides a function toolkit to facilitate reproducible RNA-Seq Differential Gene Expression (DGE)
    analysis (Law (2015) <doi:10.12688/f1000research.9005.3>).  The tools include both analysis 
    work-flow and utility functions: mapping/unit conversion, count normalization, accounting for 
    unknown covariates, and more.  This is a complement/cohort to the 'DGEobj' package that 
    provides a flexible container to manage and annotate Differential Gene Expression analysis results.
	"""
	
	cran = "DGEobj.utils" 

	version("1.0.6", md5="8acaeb2945ce80bd2f83f88ef365c88f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dgeobj@1.0.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
