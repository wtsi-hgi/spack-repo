# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSipmg(RPackage):
	"""Statistical Analysis to Identify Isotope Incorporating MAGs

	Statistical analysis as part of a stable isotope probing (SIP) metagenomics study to identify isotope incorporating taxa recovered as metagenome-assembled genomes (MAGs). 
    Helpful reading and a vignette in bookdown format is provided on the package site <https://zielslab.github.io/SIPmg.github.io/>.
	"""
	
	homepage = "https://zielslab.github.io/SIPmg.github.io/"
	cran = "SIPmg" 

	version("1.4.1", md5="412d977ba2afee738a5bdc6816d5aff9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htssip", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
