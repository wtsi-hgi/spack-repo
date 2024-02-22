# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaTools(RPackage):
	"""Comprehensive Library for Working with Missing (NA) Values in
Vectors

	
    This comprehensive toolkit provide a consistent and 
    extensible framework for working with missing values in vectors. The 
    companion package 'tidyimpute' provides similar functionality for list-like 
    and table-like structures).
    Functions exist for detection, removal, replacement, imputation, 
    recollection, etc. of 'NAs'.
	"""
	
	homepage = "https://github.com/decisionpatterns/na.tools"
	cran = "na.tools" 

	version("0.3.1", md5="f1b5a2d11d6b90f3e91a98994e318619")

	depends_on("r@3.1:", type=("build", "run"))
