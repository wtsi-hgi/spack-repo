# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmdfun(RPackage):
	"""Framework for Building Interfaces to Shell Commands

	Writing interfaces to command line software is cumbersome. 
    'cmdfun' provides a framework for building function calls to seamlessly 
    interface with shell commands by allowing lazy evaluation of command line arguments. 
    'cmdfun' also provides methods for handling user-specific paths to tool installs or secrets like API keys. 
    Its focus is to equally serve package builders who wish to wrap command line software, and to help analysts stay inside 
    R when they might usually leave to execute non-R software.
	"""
	
	homepage = "https://snystrom.github.io/cmdfun/"
	cran = "cmdfun" 

	version("1.0.2", md5="0f8c355dbb7bc7c6bd359af0be62405c")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
