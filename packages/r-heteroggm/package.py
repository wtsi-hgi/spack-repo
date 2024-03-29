# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeteroggm(RPackage):
	"""Gaussian Graphical Model-Based Heterogeneity Analysis

	The goal of this package is to user-friendly realizing Gaussian 
             graphical model-based heterogeneity analysis.
             Recently, several Gaussian graphical model-based heterogeneity 
             analysis techniques have been developed. A common methodological limitation 
             is that the number of subgroups is assumed to be known a priori, which 
             is not realistic. In a very recent study (Ren et al., 2022), a novel approach 
             based on the penalized fusion technique is developed to fully 
             data-dependently determine the number and structure of subgroups in 
             Gaussian graphical model-based heterogeneity analysis. It opens the door for utilizing 
             the Gaussian graphical model technique in more practical settings. Beyond 
             Ren et al. (2022), more estimations and functions are added, so 
             that the package is self-contained and more comprehensive and can 
             provide ``more direct'' insights to practitioners (with the 
             visualization function). Reference: 
             Ren, M., Zhang S., Zhang Q. and Ma S. (2022). Gaussian Graphical 
             Model-based Heterogeneity Analysis via Penalized Fusion. 
             Biometrics, 78 (2), 524-535.
	"""
	
	cran = "HeteroGGM" 

	version("1.0.1", md5="b24e790ef2b6cca28e6a32e1d0a76e67")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
