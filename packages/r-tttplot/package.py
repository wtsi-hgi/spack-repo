# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTttplot(RPackage):
	"""Time to Target Plot

	Implementation of Time to Target plot based on the work 
             of Ribeiro and Rosseti (2015) <DOI:10.1007/s11590-014-0760-8>, 
             that describe a numerical method that gives the probability of 
             an algorithm A finds a solution at least as good as a given 
             target value in smaller computation time than algorithm B.
	"""
	
	cran = "tttplot" 

	version("1.1.1", md5="69fe87eef7a89224197bc0fdae67a2a7")

