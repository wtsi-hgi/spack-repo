# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettycode(RPackage):
	"""Pretty Print R Code in the Terminal

	Replace the standard print method for functions with one that
    performs syntax highlighting, using ANSI colors, if the terminal
    supports them.
	"""
	
	homepage = "https://github.com/r-lib/prettycode#readme"
	cran = "prettycode" 

	version("1.1.0", md5="b191610d621d51c774f1c72b4f2faa70")

	depends_on("r-crayon", type=("build", "run"))
