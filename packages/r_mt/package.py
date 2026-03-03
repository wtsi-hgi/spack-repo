# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMt(RPackage):
	"""Metabolomics Data Analysis Toolbox

	Functions for metabolomics data analysis: data preprocessing, 
  orthogonal signal correction, PCA analysis, PCA-DA analysis, 
	PLS-DA analysis, classification, feature selection, correlation 
	analysis, data visualisation and re-sampling strategies.
	"""
	
	homepage = "https://github.com/wanchanglin/mt"
	cran = "mt" 

	version("2.0-1.20", md5="7aa9280b53599eb30167229cdbeaee6c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
