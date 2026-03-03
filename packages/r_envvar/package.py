# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvvar(RPackage):
	"""Make Working with Environment Variables Easier and More
Consistent

	A collection of functions that allows for easy and consistent use
  of environment variables. This includes setting, checking, retrieving,
  transforming, and validating values stored in environment variables.
	"""
	
	homepage = "https://github.com/briandconnelly/envvar"
	cran = "envvar" 

	version("0.1.1", md5="dd61d3d93dfa93d6fbaa81e2abcc7f72")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
