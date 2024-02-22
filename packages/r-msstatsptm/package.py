# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsptm(RPackage):
	"""Statistical Characterization of Post-translational Modifications

	MSstatsPTM provides general statistical methods for quantitative characterization of post-translational modifications (PTMs). Supports DDA, DIA, SRM, and tandem mass tag (TMT) labeling. Typically, the analysis involves the quantification of PTM sites (i.e., modified residues) and their corresponding proteins, as well as the integration of the quantification results. MSstatsPTM provides functions for summarization, estimation of PTM site abundance, and detection of changes in PTMs across experimental conditions.
	"""
	
	bioc = "MSstatsPTM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MSstatsPTM_2.4.4.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MSstatsPTM/MSstatsPTM_2.4.4.tar.gz"]

	version("2.4.4", md5="230dd6c4c447163e3575a032c7ce9667")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-msstatstmt", type=("build", "run"))
	depends_on("r-msstatsconvert", type=("build", "run"))
	depends_on("r-msstats", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
