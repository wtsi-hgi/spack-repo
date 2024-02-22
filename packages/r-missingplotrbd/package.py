# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissingplotrbd(RPackage):
	"""Missing Plot in RBD

	A system for Analysis of RBD when there is one missing observation. Methods for this process is described in A.M.Gun,M.K.Gupta,B.Dasgupta(2019,ISBN:81-87567-81-3).
	"""
	
	cran = "MissingPlotRBD" 

	version("1.1.0", md5="ddbb3253a33cc27f3bba2af3d37118f6")

