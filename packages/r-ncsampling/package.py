# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcsampling(RPackage):
	"""Nearest Centroid (NC) Sampling

	Provides functionality for performing Nearest Centroid (NC) Sampling. The NC sampling procedure was developed for forestry applications and selects plots for ground measurement so as to maximize the efficiency of imputation estimates. It uses multiple auxiliary variables and multivariate clustering to search for an optimal sample. Further details are given in Melville G. & Stone C. (2016) <doi:10.1080/00049158.2016.1218265>. 
	"""
	
	cran = "NCSampling" 

	version("1.0", md5="dcde36779bbe26d126016e17bb1879ef")

	depends_on("r-yaimpute", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
