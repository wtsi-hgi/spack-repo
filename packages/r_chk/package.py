# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChk(RPackage):
	"""Check User-Supplied Function Arguments

	For developers to check user-supplied function arguments.  It
    is designed to be simple, fast and customizable.  Error messages
    follow the tidyverse style guide.
	"""
	
	homepage = "https://poissonconsulting.github.io/chk/"
	cran = "chk" 

	version("0.9.1", md5="9675ddf805c4166e42173d2b773b8a38")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
