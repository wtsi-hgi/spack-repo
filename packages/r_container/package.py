# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContainer(RPackage):
	"""Extending Base 'R' Lists

	Extends the functionality of base 'R' lists and
    provides specialized data structures 'deque',
    'set', 'dict', and 'dict.table', the latter to extend the 'data.table'
    package.
	"""
	
	homepage = "https://rpahl.github.io/container/"
	cran = "container" 

	version("1.0.4", md5="3d5b5e9be0cb5383184a93b3be6a9605")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
