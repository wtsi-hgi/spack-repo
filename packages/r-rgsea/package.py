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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RGSEA_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RGSEA/RGSEA_1.36.0.tar.gz"]

	version("1.36.0", md5="426ab6d4dc463399d014c6e76c3f8c75")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
