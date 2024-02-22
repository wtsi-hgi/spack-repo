# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPetests(RPackage):
	"""Power-Enhanced (PE) Tests for High-Dimensional Data

	Two-sample power-enhanced mean tests, covariance tests, and simultaneous tests on mean vectors and covariance matrices for high-dimensional data. Methods of these PE tests are presented in 
    Yu, Li, and Xue (2022) <doi:10.1080/01621459.2022.2126781>; 
    Yu, Li, Xue, and Li (2022) <doi:10.1080/01621459.2022.2061354>.
	"""
	
	cran = "PEtests" 

	version("0.1.0", md5="02ba4ab0e28f489847886fd5b387d81c")

