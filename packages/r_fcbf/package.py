# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcbf(RPackage):
	"""Fast Correlation Based Filter for Feature Selection

	This package provides a simple R implementation for the Fast Correlation Based Filter described in Yu, L. and Liu, H.; Feature Selection for High-Dimensional Data: A Fast Correlation Based Filter Solution,Proc. 20th Intl. Conf. Mach. Learn. (ICML-2003), Washington DC, 2003 The current package is an intent to make easier for bioinformaticians to use FCBF for feature selection, especially regarding transcriptomic data.This implies discretizing expression (function discretize_exprs) before calculating the features that explain the class, but are not predictable by other features. The functions are implemented based on the algorithm of Yu and Liu, 2003 and Rajarshi Guha's implementation from 13/05/2005 available (as of 26/08/2018) at http://www.rguha.net/code/R/fcbf.R .
	"""
	
	bioc = "FCBF" 

	version("2.10.0", commit="9deb5d7bb0671b786d319cbae6ffbcb82976eb0e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
