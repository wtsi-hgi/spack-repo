# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazybar(RPackage):
	"""Progress Bar with Remaining Time Forecast Method

	A simple progress bar showing estimated remaining time. 
    Multiple forecast methods and user defined forecast method for 
    the remaining time are supported.
	"""
	
	homepage = "https://pkg.yangzhuoranyang.com/lazybar/"
	cran = "lazybar" 

	version("0.1.0", md5="d98c5ad2b39b7be13115df4cf7fa5358")

	depends_on("r-r6", type=("build", "run"))
