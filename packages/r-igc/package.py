# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgc(RPackage):
	"""An integrated analysis package of Gene expression and Copy number alteration

	This package is intended to identify differentially expressed genes driven by Copy Number Alterations from samples with both gene expression and CNA data.
	"""
	
	homepage = "http://github.com/ccwang002/iGC"
	bioc = "iGC"

	version("1.38.0", commit="0b6c595d9a450e18c0d29ef114f0f5c0626a08bc")
	version("1.32.0", commit="18e7fd25f3b3037861243b76930d03933daa5ef8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
