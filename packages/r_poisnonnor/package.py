# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisnonnor(RPackage):
	"""Simultaneous Generation of Count and Continuous Data

	Generation of count (assuming Poisson distribution) and continuous data (using Fleishman polynomials) simultaneously. The details of the method are explained in Demirtas et al. (2012) <DOI:10.1002/sim.5362>. 
	"""
	
	cran = "PoisNonNor" 

	version("1.6.3", md5="03b303ef9a1282a0996fbc9e40483a97")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
