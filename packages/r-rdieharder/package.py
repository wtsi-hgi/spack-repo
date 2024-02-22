# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdieharder(RPackage):
	"""R Interface to the 'DieHarder' RNG Test Suite

	The 'RDieHarder' package provides an R interface to 
 the 'DieHarder' suite of random number generators and tests that 
 was developed by Robert G. Brown and David Bauer, extending 
 earlier work by George Marsaglia and others. The 'DieHarder'
 library code is included.
	"""
	
	homepage = "https://github.com/eddelbuettel/rdieharder"
	cran = "RDieHarder" 

	version("0.2.6", md5="a36fe037ea7df7e4caf0e953d149deb5")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
