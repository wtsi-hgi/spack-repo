# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgsea(RPackage):
	"""Random Gene Set Enrichment Analysis

	Combining bootstrap aggregating and Gene set enrichment analysis (GSEA), RGSEA is a classfication algorithm with high robustness and no over-fitting problem. It performs well especially for the data generated from different exprements.
	"""
	
	bioc = "RGSEA"

	version("1.42.0", commit="bb32b4ad79a8bc945c87170b91f53c7af0337fa0")
	version("1.36.0", commit="b4f59d92e6e6a7db3e49bea926083778b4b3bf87")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
