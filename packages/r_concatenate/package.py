# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcatenate(RPackage):
	"""Human-Friendly Text from Unknown Strings

	Simple functions for joining strings. Construct human-friendly messages whose elements aren't known in advance, like in stop, warning, or message, from clean code.
	"""
	
	homepage = "https://github.com/jamesdunham/concatenate"
	cran = "concatenate" 

	version("1.0.0", md5="a2550368042163ddb64577dcbc47ba7c")

	depends_on("r@3.1:", type=("build", "run"))
