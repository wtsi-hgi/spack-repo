# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REponge(RPackage):
	"""Keep Your Environment Clean

	Provides a set of functions, which facilitates removing objects from an environment. 
             It allows to delete objects specified with regular expression or with other conditions (e.g. if object is numeric),
             using one function call.    
	"""
	
	homepage = "https://github.com/krzjoa/eponge"
	cran = "eponge" 

	version("0.1.0", md5="84f5a5e543674f717e5ea1051555f359")

	depends_on("r-rlang", type=("build", "run"))
