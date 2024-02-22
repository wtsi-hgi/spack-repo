# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonpar(RPackage):
	"""A Collection of Nonparametric Hypothesis Tests

	Contains the following 5 nonparametric hypothesis tests:
    The Sign Test,
    The 2 Sample Median Test,
    Miller's Jackknife Procedure,
    Cochran's Q Test, &
    The Stuart-Maxwell Test.
	"""
	
	cran = "nonpar" 

	version("1.0.2", md5="b12a4dcb29cd5b0a0c9ce595f21f83cb")

	depends_on("r@3.3.1:", type=("build", "run"))
