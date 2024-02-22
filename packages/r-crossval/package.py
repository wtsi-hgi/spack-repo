# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossval(RPackage):
	"""Generic Functions for Cross Validation

	Contains generic functions for performing 
  cross validation and for computing diagnostic errors.
	"""
	
	homepage = "https://cran.r-project.org/package=crossval"
	cran = "crossval" 

	version("1.0.5", md5="e39e56621b8b58660994c91c98d7ec51")

	depends_on("r@3.0.2:", type=("build", "run"))
