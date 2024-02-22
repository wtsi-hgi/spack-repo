# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicspls(RPackage):
	"""Data Integration with Two-Way Orthogonal Partial Least Squares

	Performs the O2PLS data integration method for two datasets, yielding joint and data-specific parts for each dataset.
    The algorithm automatically switches to a memory-efficient approach to fit O2PLS to high dimensional data.
    It provides a rigorous and a faster alternative cross-validation method to select the number of components,
    as well as functions to report proportions of explained variation and to construct plots of the results. 
    See the software article by el Bouhaddani et al (2018) <doi:10.1186/s12859-018-2371-3>, 
    and Trygg and Wold (2003) <doi:10.1002/cem.775>.
    It also performs Sparse Group (Penalized) O2PLS, see Gu et al (2020) <doi:10.1186/s12859-021-03958-3> and cross-validation for the degree of sparsity. 
	"""
	
	cran = "OmicsPLS" 

	version("2.0.2", md5="894f220590ea6c96f8ec4e7d039b39a0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
