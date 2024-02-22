# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfs(RPackage):
	"""Tool for Ensemble Feature Selection

	Provides a function to check the
  importance of a feature based on a dependent classification
  variable. An ensemble of feature selection methods
  is used to determine the normalized importance value of
  all features. Combining these methods in one function
  (building the cumulative importance values) provides a 
  stable feature selection tool. This selection
  can also be viewed in a barplot using the barplot_fs() function
  and proved using the evaluation function efs_eval().
	"""
	
	cran = "EFS" 

	version("1.0.3", md5="116d3bb0a5483a2cfe5aeb42c1632a02")

	depends_on("r-party", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
