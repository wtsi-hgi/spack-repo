# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairviz(RPackage):
	"""Visualization using Graph Traversal

	Improving graphics by ameliorating order effects, using Eulerian tours 
    and Hamiltonian decompositions of  graphs. References for the methods presented 
    here are C.B. Hurley and R.W. Oldford (2010) <doi:10.1198/jcgs.2010.09136> and 
    C.B. Hurley and R.W. Oldford (2011) <doi:10.1007/s00180-011-0229-5>.
	"""
	
	homepage = "https://cbhurley.github.io/PairViz/"
	cran = "PairViz" 

	version("1.3.6", md5="54f3e4f29aa46b071b75d2143f3968b5")

	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
