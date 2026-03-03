# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROppar(RPackage):
	"""Outlier profile and pathway analysis in R

	The R implementation of mCOPA package published by Wang et al. (2012). Oppar provides methods for Cancer Outlier profile Analysis. Although initially developed to detect outlier genes in cancer studies, methods presented in oppar can be used for outlier profile analysis in general. In addition, tools are provided for gene set enrichment and pathway analysis.
	"""
	
	bioc = "oppar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/oppar_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/oppar/oppar_1.30.0.tar.gz"]

	version("1.30.0", md5="21adf37b9236cf860009e709f63d5e30")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
