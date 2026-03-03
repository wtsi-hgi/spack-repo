# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErify(RPackage):
	"""Check Arguments and Generate Readable Error Messages

	Provides several validator functions for checking if arguments
    passed by users have valid types, lengths, etc. and for generating
    informative and well-formatted error messages in a consistent style. Also
    provides tools for users to create their own validator functions. The
    error message style used is adopted from
    <https://style.tidyverse.org/error-messages.html>.
	"""
	
	homepage = "https://github.com/flujoo/erify"
	cran = "erify" 

	version("0.4.0", md5="cf82e07d597b960f2b942fc18d602f65")

	depends_on("r-glue", type=("build", "run"))
