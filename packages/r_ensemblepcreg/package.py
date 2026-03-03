# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblepcreg(RPackage):
	"""Extensible Package for Principal-Component-Regression-Based
Heterogeneous Ensemble Meta-Learning

	Extends the base classes and methods of 'EnsembleBase' package for Principal-Components-Regression-based (PCR) integration of base learners. Default implementation uses cross-validation error to choose the optimal number of PC components for the final predictor. The package takes advantage of the file method provided in 'EnsembleBase' package for writing estimation objects to disk in order to circumvent RAM bottleneck. Special save and load methods are provided to allow estimation objects to be saved to permanent files on disk, and to be loaded again into temporary files in a later R session. Users and developers can extend the package by extending the generic methods and classes provided in 'EnsembleBase' package as well as this package.
	"""
	
	cran = "EnsemblePCReg" 

	version("1.1.4", md5="8bcf57fd703103d05c1c6d0fb8cf0743")

	depends_on("r-ensemblebase", type=("build", "run"))
