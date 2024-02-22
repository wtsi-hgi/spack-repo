# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprintf(RPackage):
	"""Adaptive Builder for Formatted Strings

	Provides a set of functions to facilitate building formatted strings
    under various replacement rules: C-style formatting, variable-based formatting,
    and number-based formatting. C-style formatting is basically identical to built-in
    function 'sprintf'. Variable-based formatting allows users to put variable names
    in a formatted string which will be replaced by variable values. Number-based
    formatting allows users to use index numbers to represent the corresponding
    argument value to appear in the string.
	"""
	
	homepage = "http://renkun.me/rprintf"
	cran = "rprintf" 

	version("0.2.1", md5="3742a47b3a641becd27860aae2b3ed16")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
