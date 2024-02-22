# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApachelogprocessor(RPackage):
	"""Process the Apache Web Server Log Files

	Provides capabilities to process Apache HTTPD Log files.The main functionalities are to extract data from access and error log files to data frames.
	"""
	
	homepage = "https://github.com/diogosmendonca/ApacheLogProcessor"
	cran = "ApacheLogProcessor" 

	version("0.2.3", md5="2482f904d3ba80bb3f04278396e883c4")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
