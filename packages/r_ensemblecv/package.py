# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnsemblecv(RPackage):
	"""Extensible Package for Cross-Validation-Based Integration of
Base Learners

	Extends the base classes and methods of EnsembleBase package for cross-validation-based integration of base learners. Default implementation calculates average of repeated CV errors, and selects the base learner / configuration with minimum average error. The package takes advantage of the file method provided in EnsembleBase package for writing estimation objects to disk in order to circumvent RAM bottleneck. Special save and load methods are provided to allow estimation objects to be saved to permanent files on disk, and to be loaded again into temporary files in a later R session. The package can be extended, e.g. by adding variants of the current implementation.
	"""
	
	cran = "EnsembleCV" 

	version("0.8", md5="f2858ead070d9abfc7bab02a68d55d28")

	depends_on("r-ensemblebase", type=("build", "run"))
