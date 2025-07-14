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

	version("1.34.0", commit="8f40efd3bb7f6a366b533d3caece67c00173fcf1")
	version("1.28.0", commit="55ba684eaf402d02a41a369960577443468be358")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
