# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzym(RPackage):
	"""Fuzzy Cognitive Maps Operations

	Contains functions for operations with fuzzy cognitive maps using t-norm and s-norm operators. T-norms and S-norms are described by Dov M. Gabbay and George Metcalfe (2007) <doi:10.1007/s00153-007-0047-1>. System indicators are described by Cox, Earl D. (1995) <isbn:1886801010>. Executable examples are provided in the "inst/examples" folder.
	"""
	
	cran = "FuzzyM" 

	version("0.1.0", md5="86ff5b4778855a3bec1a37e3848cd9af")

