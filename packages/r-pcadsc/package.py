# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcadsc(RPackage):
	"""Tools for Principal Component Analysis-Based Data Structure
Comparisons

	A suite of non-parametric, visual tools for assessing differences in data structures
    for two datasets that contain different observations of the same variables. These tools are all 
    based on Principal Component Analysis (PCA) and thus effectively address differences in the structures
    of the covariance matrices of the two datasets. The PCASDC tools consist of easy-to-use, 
    intuitive plots that each focus on different aspects of the PCA decompositions. The cumulative eigenvalue
    (CE) plot describes differences in the variance components (eigenvalues) of the deconstructed covariance matrices. The
    angle plot presents the information loss when moving from the PCA decomposition of one dataset to the 
    PCA decomposition of the other. The chroma plot describes the loading patterns of the two datasets, thereby
    presenting the relative weighting and importance of the variables from the original dataset. 
	"""
	
	homepage = "https://github.com/annepetersen1/PCADSC"
	cran = "PCADSC" 

	version("0.8.0", md5="dface65ea5feae269037e08f1c1e4421")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
