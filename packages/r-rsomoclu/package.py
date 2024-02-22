# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsomoclu(RPackage):
	"""Somoclu

	Somoclu is a massively parallel implementation of self-organizing maps.  It exploits multicore CPUs and it can be accelerated by CUDA. The topology of the map can be planar or toroid and the grid of neurons can be rectangular or hexagonal . Details refer to (Peter Wittek, et al (2017)) <doi:10.18637/jss.v078.i09>.
	"""
	
	homepage = "https://peterwittek.github.io/somoclu/"
	cran = "Rsomoclu" 

	version("1.7.6", md5="8cc12b038c68cc442a10775c6ba4260a")

	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
