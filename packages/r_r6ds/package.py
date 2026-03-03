# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR6ds(RPackage):
	"""R6 Reference Class Based Data Structures

	Provides reference classes implementing some useful data structures.
    The package implements these data structures by using the reference class R6.
    Therefore, the classes of the data structures are also reference classes which means that their instances are passed by reference.
    The implemented data structures include stack, queue, double-ended queue, doubly linked list, set, dictionary and binary search tree.
    See for example <https://en.wikipedia.org/wiki/Data_structure> for more information about the data structures.
	"""
	
	homepage = "https://github.com/yukai-yang/R6DS"
	cran = "R6DS" 

	version("1.2.0", md5="e71eee43b332a7edb2a915c5462c69f5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
