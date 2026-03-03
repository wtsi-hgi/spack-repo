# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRing(RPackage):
	"""Circular / Ring Buffers

	Circular / ring buffers in R and C.  There are a couple
    of different buffers here with different implementations that
    represent different trade-offs.
	"""
	
	homepage = "https://github.com/mrc-ide/ring"
	cran = "ring" 

	version("1.0.5", md5="22146475eb756ee278ae2430174116f4")

	depends_on("r-r6", type=("build", "run"))
