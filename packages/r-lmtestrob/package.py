# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmtestrob(RPackage):
	"""Outlier Robust Specification Testing

	Robust test(s) for model diagnostics in regression. The current version contains a robust test for functional specification (linearity). The test is based on the robust bounded-influence test by Heritier and Ronchetti (1994) <doi:10.1080/01621459.1994.10476822>.
	"""
	
	cran = "lmtestrob" 

	version("0.1", md5="bc5418f13bdcf216ca4c47eafaa8b876")

	depends_on("r-mass", type=("build", "run"))
