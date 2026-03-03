# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobial(RPackage):
	"""Do 16s Data Analysis and Generate Figures

	Provides functions to enhance the available 
            statistical analysis procedures in R by providing simple functions to 
            analysis and visualize the 16S rRNA data.Here we present a tutorial 
            with minimum working examples to demonstrate usage and dependencies. 
	"""
	
	cran = "microbial" 

	version("0.0.20", md5="578f3759e616e5b1952ad4430b400203")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
