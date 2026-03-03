# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreats(RPackage):
	"""Trees and Traits Simulations

	A modular package for simulating phylogenetic trees and species traits jointly. Trees can be simulated using modular birth-death parameters (e.g. changing starting parameters or algorithm rules). Traits can be simulated in any way designed by the user. The growth of the tree and the traits can influence each other through modifiers objects providing rules for affecting each other. Finally, events can be created to modify both the tree and the traits under specific conditions. 
	"""
	
	homepage = "https://github.com/TGuillerme/treats"
	cran = "treats" 

	version("1.0", md5="c5c8034748f4f53e2d76defb6e28b916")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-disprity", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
