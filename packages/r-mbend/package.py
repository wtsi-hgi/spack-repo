# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbend(RPackage):
	"""Matrix Bending

	Bending non-positive-definite (symmetric) matrices to positive-definite, using weighted and unweighted methods.
   Jorjani, H., et al. (2003) <doi:10.3168/jds.S0022-0302(03)73646-7>.
   Schaeffer, L. R. (2014) <http://animalbiosciences.uoguelph.ca/~lrs/ELARES/PDforce.pdf>.
	"""
	
	homepage = "https://github.com/nilforooshan/mbend"
	cran = "mbend" 

	version("1.3.1", md5="88b2866e9b1b0bde9e4ad74c404cbfcf")

