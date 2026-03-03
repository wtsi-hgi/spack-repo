# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatskew(RPackage):
	"""Matrix Skew-T Parameter Estimation

	Performs matrix skew-t parameter estimation, Gallaugher and McNicholas (2017)  <doi: 10.1002/sta4.143>.
	"""
	
	cran = "MatSkew" 

	version("0.1.5", md5="2a1dd20c7904d4641ecb71c29ad0dffe")

