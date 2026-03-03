# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCb2(RPackage):
	"""CRISPR Pooled Screen Analysis using Beta-Binomial Test

	Provides functions for hit gene identification and quantification of sgRNA (single-guided RNA) abundances for CRISPR (Clustered Regularly Interspaced Short Palindromic Repeats) pooled screen data analysis. 
  Details are in Jeong et al. (2019) <doi:10.1101/gr.245571.118> and Baggerly et al. (2003) <doi:10.1093/bioinformatics/btg173>. 
	"""
	
	cran = "CB2" 

	version("1.3.4", md5="b44f66f1a017b543b0d1d52e2a6605fa", url="https://cran.r-project.org/src/contrib/CB2_1.3.4.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
