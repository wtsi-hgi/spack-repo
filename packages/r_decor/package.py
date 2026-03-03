# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecor(RPackage):
	"""Retrieve Code Decorations

	Retrieves code comment decorations for C++
    languages of the form ' [[xyz]]', which are used for automated
    wrapping of C++ functions.
	"""
	
	homepage = "https://github.com/r-lib/decor"
	cran = "decor" 

	version("1.0.2", md5="b804d7c8cd20cfffc84e4c0bcb194e58")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
