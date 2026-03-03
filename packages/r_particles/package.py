# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParticles(RPackage):
	"""A Graph Based Particle Simulator Based on D3-Force

	Simulating particle movement in 2D space has many application. The
    'particles' package implements a particle simulator based on the ideas 
    behind the 'd3-force' 'JavaScript' library. 'particles' implements all 
    forces defined in 'd3-force' as well as others such as vector fields, traps, 
    and attractors.
	"""
	
	homepage = "https://github.com/thomasp85/particles"
	cran = "particles" 

	version("0.2.3", md5="9884edd12e151bfe83b5715e807d8835")

	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
