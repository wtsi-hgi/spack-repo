# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoltest(RPackage):
	"""Community Ecology Tests

	Functions and data sets to perform and demonstrate community ecology statistical tests, including Hutcheson's t-test (Hutcheson (1970) <doi:10.1016/0022-5193(70)90124-4>, Zar (2010) ISBN:9780321656865). 
	"""
	
	homepage = "https://github.com/hugosal/ecolTest"
	cran = "ecolTest" 

	version("0.0.1", md5="f79d397cef835b543340bedb0c102dc1")

	depends_on("r@2.10:", type=("build", "run"))
