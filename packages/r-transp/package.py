# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransp(RPackage):
	"""Implementation of Transportation Problem Algorithms

	Implementation of two transportation problem algorithms. 
             1. North West Corner Method 
             2. Minimum Cost Method or Least cost method.
             For more technical details about the algorithms please refer below URLs.
             <http://www.universalteacherpublications.com/univ/ebooks/or/Ch5/nw.htm>.
             <http://personal.maths.surrey.ac.uk/st/J.F/chapter7.pdf>.
	"""
	
	homepage = "https://github.com/Somenath24/TransP"
	cran = "TransP" 

	version("0.1", md5="15fdd5a549940f6518bf489b3a97b5d3")

