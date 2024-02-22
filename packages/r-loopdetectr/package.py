# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoopdetectr(RPackage):
	"""Comprehensive Feedback Loop Detection in ODE Models

	Detect feedback loops (cycles, circuits) between species (nodes) in ordinary differential equation (ODE) models. Feedback loops are paths from a node to itself without visiting any other node twice, and they have important regulatory functions. Loops are reported with their order of participating nodes and their length, and whether the loop is a positive or a negative feedback loop. An upper limit of the number of feedback loops limits runtime (which scales with feedback loop count). Model parametrizations and values of the modelled variables are accounted for. Computation uses the characteristics of the Jacobian matrix as described e.g. in Thomas and Kaufman (2002) <doi:10.1016/s1631-0691(02)01452-x>. Input can be the Jacobian matrix of the ODE model or the ODE function definition; in the latter case, the Jacobian matrix is determined using 'numDeriv'. Graph-based algorithms from 'igraph' are employed for path detection. 
	"""
	
	cran = "LoopDetectR" 

	version("0.1.2", md5="3b117f8222d6ebd76fb4ee67c15051bf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
