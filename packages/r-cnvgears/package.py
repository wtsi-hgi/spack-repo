# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvgears(RPackage):
	"""A Framework of Functions to Combine, Analize and Interpret CNVs Calling Results

	This package contains a set of functions to perform several type of processing and analysis on CNVs calling pipelines/algorithms results in an integrated manner and regardless of the raw data type (SNPs array or NGS). It provides functions to combine multiple CNV calling results into a single object, filter them, compute CNVRs (CNV Regions) and inheritance patterns, detect genic load, and more. The package is best suited for studies in human family-based cohorts.
	"""
	
	bioc = "CNVgears" 

	version("1.10.0", commit="69f92024f206b6aa1e49306f2456174925788caf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
