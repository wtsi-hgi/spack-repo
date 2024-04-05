# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogr(RPackage):
	"""Creates Log Files

	Contains functions to help create log files.  The 
    package aims to overcome the difficulty of the base R sink() command.  The
    log_print() function will print to both the console and the file log, 
    without interfering in other write operations.
	"""
	
	homepage = "https://logr.r-sassy.org"
	cran = "logr" 

	version("1.3.6", md5="e347e49e53c58d8a84418e608d94debe")
	version("1.3.5", md5="6b216952470eee98af6641ad8a816f97")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-common", type=("build", "run"))
