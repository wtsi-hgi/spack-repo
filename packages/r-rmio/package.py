# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RRmio(RPackage):
	"""Provides 'mio' C++11 Header Files

	Provides header files of 'mio', a cross-platform C++11 header-only 
    library for memory mapped file IO <https://github.com/mandreyel/mio>.
	"""
	
	homepage = "https://github.com/privefl/rmio"
	cran = "rmio" 

	version("0.4.0", md5="314ac4ca6cb6fed581e2e13211124262")

	depends_on("r-bigassertr", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
