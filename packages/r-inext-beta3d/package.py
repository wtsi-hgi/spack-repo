# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInextBeta3d(RPackage):
	"""Interpolation and Extrapolation with Beta Diversity for Three
Dimensions of Biodiversity

	As a sequel to 'iNEXT', the 'iNEXT.beta3D' package provides functions to compute 
              standardized taxonomic, phylogenetic, and functional diversity (3D) estimates 
              with a common sample size (for alpha and gamma diversity) or sample coverage 
              (for alpha, beta, gamma diversity as well as dissimilarity or turnover indices). 
              Hill numbers and their generalizations are used to quantify 3D and to make 
              multiplicative decomposition (gamma = alpha x beta). The package also features 
              size- and coverage-based rarefaction and extrapolation sampling curves to 
              facilitate rigorous comparison of beta diversity across datasets.  
              See Chao et al. (2023) <doi:10.1002/ecm.1588> for more details.
	"""
	
	homepage = "https://sites.google.com/view/chao-lab-website/software/inext-beta3d"
	cran = "iNEXT.beta3D" 

	version("1.0.0", md5="4bc7a9119ef51985a0bec6ec655cec0c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-inext-3d", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidytree", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-phyclust", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
