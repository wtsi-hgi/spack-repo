# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertions(RPackage):
	"""Simple Assertions for Beautiful and Customisable Error Messages

	Provides simple assertions with sensible defaults and customisable error messages. 
  It offers convenient assertion call wrappers and a general assert function that can handle any condition.
  Default error messages are user friendly and easily customized with inline code evaluation and styling powered by the 'cli' package.
	"""
	
	homepage = "https://github.com/selkamand/assertions"
	cran = "assertions" 

	version("0.1.0", md5="f34e0610b60ffe7706ebefea4bb9b5bd")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
