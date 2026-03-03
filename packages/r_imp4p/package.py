# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImp4p(RPackage):
	"""Imputation for Proteomics

	Functions to analyse missing value mechanisms and to impute data sets in the context of bottom-up MS-based proteomics.
	"""
	
	cran = "imp4p" 

	version("1.2", md5="434f2f7cf00561eafe40d992b890a27c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-missmda", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
