# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSispa(RPackage):
	"""SISPA: Method for Sample Integrated Set Profile Analysis

	Sample Integrated Set Profile Analysis (SISPA) is a method designed to define sample groups with similar gene set enrichment profiles.
	"""
	
	bioc = "SISPA" 

	version("1.32.0", commit="3ad0c59577c3b7ae3060cfabfcbb6b4a4b3180ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
