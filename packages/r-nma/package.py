# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNma(RPackage):
	"""Network Meta-Analysis Based on Multivariate Meta-Analysis Models

	Network meta-analysis tools based on contrast-based approach using the multivariate meta-analysis and meta-regression models (Noma et al. (2023) <Forthcoming>). Standard analysis tools for network meta-analysis and meta-regression (e.g., synthesis analysis, ranking analysis, and creating league table) are available by simple commands. For inconsistency analyses, the local and global inconsistency tests based on the Higgins' design-by-treatment interaction model can be applied. Also, the side-splitting and the Jackson's random inconsistency model are available. Standard graphical tools for network meta-analysis (e.g., network plot, ranked forest plot, and transitivity analysis) can also be utilized. For the synthesis analyses, the Noma-Hamura's improved REML (restricted maximum likelihood)-based methods (Noma et al. (2023) <doi:10.1002/jrsm.1652> <doi:10.1002/jrsm.1651>) are adopted as the default methods. 
	"""
	
	homepage = "https://www.ism.ac.jp/~noma/file/software/NMA.r"
	cran = "NMA" 

	version("1.4-2", md5="b11b20e6c5261f1ee4b103d9b42c2cbd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
