# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiostat3(RPackage):
	"""Utility Functions, Datasets and Extended Examples for Survival
Analysis

	Utility functions, datasets and extended examples for survival analysis. This extends a range of other packages, some simple wrappers for time-to-event analyses, datasets, and extensive examples in HTML with R scripts. The package also supports the course Biostatistics III entitled "Survival analysis for epidemiologists in R".
	"""
	
	cran = "biostat3" 

	version("0.1.9", md5="53483339aa534f9ac10a44746b539a5b", url="https://cran.r-project.org/src/contrib/biostat3_0.1.9.tar.gz")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-muhaz", type=("build", "run"))
