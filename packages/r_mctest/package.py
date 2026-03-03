# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMctest(RPackage):
	"""Multicollinearity Diagnostic Measures

	Package computes popular and widely used multicollinearity diagnostic measures <doi:10.17576/jsm-2019-4809-26> and <doi:10.32614/RJ-2016-062> . Package also indicates which regressors may be the reason of collinearity among regressors.
	"""
	
	cran = "mctest" 

	version("1.3.1", md5="b9531ef62d83a27149686880d3ae4705")

	depends_on("r@3.4:", type=("build", "run"))
