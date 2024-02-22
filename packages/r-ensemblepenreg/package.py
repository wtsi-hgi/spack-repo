# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblepenreg(RPackage):
	"""Extensible Classes and Methods for Penalized-Regression-Based
Integration of Base Learners

	Extending the base classes and methods of EnsembleBase package for Penalized-Regression-based (Ridge and Lasso) integration of base learners. Default implementation uses cross-validation error to choose the optimal lambda (shrinkage parameter) for the final predictor. The package takes advantage of the file method provided in EnsembleBase package for writing estimation objects to disk in order to circumvent RAM bottleneck. Special save and load methods are provided to allow estimation objects to be saved to permanent files on disk, and to be loaded again into temporary files in a later R session. Users and developers can extend the package by extending the generic methods and classes provided in EnsembleBase package as well as this package.
	"""
	
	cran = "EnsemblePenReg" 

	version("0.7", md5="69db11ac9e4ef069377ea6ddac54e08d")

	depends_on("r-ensemblebase", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
