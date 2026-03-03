# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmsim(RPackage):
	"""Seamless 'Nonmem' Simulation Platform

	A complete and seamless 'Nonmem' simulation interface from within R. Turns 'Nonmem' control streams into simulation control streams, executes them with specified simulation input data and returns the results. The simulation is performed by 'Nonmem', eliminating time spent and risks of re-implementation of models in other tools.
	"""
	
	homepage = "https://philipdelff.github.io/NMsim/"
	cran = "NMsim" 

	version("0.1.0", md5="569ded5aac998e16aea16e3b30f61aa4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-nmdata@0.1.3:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
