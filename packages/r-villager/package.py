# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVillager(RPackage):
	"""A Framework for Designing and Running Agent Based Models

	This is a package for creating and running Agent Based Models (ABM). It provides a set of base classes with core functionality to allow bootstrapped models. For more intensive modeling, the supplied classes can be extended to fit researcher needs.
	"""
	
	homepage = "https://github.com/zizroc/villager/"
	cran = "villager" 

	version("1.1.1", md5="0b211c7778c0383f1739b76847bccd29")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
