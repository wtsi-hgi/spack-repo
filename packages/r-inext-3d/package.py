# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInext3d(RPackage):
	"""Interpolation and Extrapolation for Three Dimensions of
Biodiversity

	Biodiversity is a multifaceted concept covering different levels of organization from
            genes to ecosystems. 'iNEXT.3D' extends 'iNEXT' to include three dimensions (3D) 
            of biodiversity, i.e., taxonomic diversity (TD), phylogenetic diversity (PD) and functional 
            diversity (FD). This package provides functions to compute standardized 3D diversity estimates 
            with a common sample size or sample coverage. A unified framework based on Hill numbers 
            and their generalizations (Hill-Chao numbers) are used to quantify 3D. All 3D estimates 
            are in the same units of species/lineage equivalents and can be meaningfully compared. 
            The package features size- and coverage-based rarefaction and extrapolation sampling 
            curves to facilitate rigorous comparison of 3D diversity across individual assemblages. 
            Asymptotic 3D diversity estimates are also provided. See Chao et al. (2021) 
            <doi:10.1111/2041-210X.13682> for more details.
	"""
	
	homepage = "https://sites.google.com/view/chao-lab-website/software/inext-3d"
	cran = "iNEXT.3D" 

	version("1.0.2", md5="cca3d726d4c9cf1add7fc01b67204390")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidytree", type=("build", "run"))
	depends_on("r-phyclust", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
