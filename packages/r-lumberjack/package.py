# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumberjack(RPackage):
	"""Track Changes in Data

	A framework that allows for easy logging of changes in data.
    Main features: start tracking changes by adding a single line of code to 
    an existing script. Track changes in multiple datasets, using multiple 
    loggers. Add custom-built loggers or use loggers offered by other 
    packages. <doi:10.18637/jss.v098.i01>.
	"""
	
	homepage = "https://github.com/markvanderloo/lumberjack"
	cran = "lumberjack" 

	version("1.3.1", md5="b1161660e92cc1c7be915269e3769d94")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
