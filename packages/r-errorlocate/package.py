# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErrorlocate(RPackage):
	"""Locate Errors with Validation Rules

	Errors in data can be located and removed using validation rules from package 
   'validate'. See also Van der Loo and De Jonge (2018) <doi:10.1002/9781118897126>,
   chapter 7.
	"""
	
	homepage = "https://github.com/data-cleaning/errorlocate"
	cran = "errorlocate" 

	version("1.1.1", md5="4ca8d0b426fb3ae0b2743f91ee504f44")

	depends_on("r-validate", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
