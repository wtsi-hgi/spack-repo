# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdpna(RPackage):
	"""Disease-Drived Differential Proteins Co-Expression Network
Analysis

	Functions designed to connect disease-related differential proteins and 
  co-expression network. It provides the basic statics analysis included t test, ANOVA analysis. 
  The network construction is not offered by the package, you can used 'WGCNA' package which you 
  can learn in Peter et al. (2008) <doi:10.1186/1471-2105-9-559>. It also provides module analysis 
  included PCA analysis, two enrichment analysis, Planner maximally filtered graph extraction and 
  hub analysis.
	"""
	
	homepage = "https://github.com/liukf10/DDPNA"
	cran = "DDPNA" 

	version("0.3.3", md5="ed50b3c5daa23f43a8e15b8d6bcfcd61")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggalt", type=("build", "run"))
	depends_on("r-megena", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
