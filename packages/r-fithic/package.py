# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFithic(RPackage):
	"""Confidence estimation for intra-chromosomal contact maps

	Fit-Hi-C is a tool for assigning statistical confidence estimates to intra-chromosomal contact maps produced by genome-wide genome architecture assays such as Hi-C.
	"""
	
	bioc = "FitHiC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/FitHiC_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/FitHiC/FitHiC_1.28.0.tar.gz"]

	version("1.28.0", md5="ee894d402d0c5567935ade4f8dc75c29")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
