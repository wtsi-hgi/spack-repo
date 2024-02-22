# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmbient(RPackage):
	"""A Generator of Multidimensional Noise

	Generation of natural looking noise has many application within 
    simulation, procedural generation, and art, to name a few. The 'ambient' 
    package provides an interface to the 'FastNoise' C++ library and allows for
    efficient generation of perlin, simplex, worley, cubic, value, and white 
    noise with optional perturbation in either 2, 3, or 4 (in case of simplex and
    white noise) dimensions.
	"""
	
	homepage = "https://ambient.data-imaginist.com"
	cran = "ambient" 

	version("1.0.2", md5="a64bff9c025364cccaf55113e688e6b0")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cpp11@0.4.2:", type=("build", "run"))
