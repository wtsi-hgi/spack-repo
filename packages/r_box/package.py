# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBox(RPackage):
	"""Write Reusable, Composable and Modular R Code

	A modern module system for R. Organise code into hierarchical,
    composable, reusable modules, and use it effortlessly across projects via a
    flexible, declarative dependency loading syntax.
	"""
	
	homepage = "https://klmr.me/box/"
	cran = "box" 

	version("1.2.0", md5="487b201d56de5c722826f572700f05f3")

	depends_on("r@3.6:", type=("build", "run"))
