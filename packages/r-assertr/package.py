# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssertr(RPackage):
	"""Assertive Programming for R Analysis Pipelines

	Provides functionality to assert conditions
    that have to be met so that errors in data used in
    analysis pipelines can fail quickly. Similar to
    'stopifnot()' but more powerful, friendly, and easier
    for use in pipelines.
	"""
	
	homepage = "https://docs.ropensci.org/assertr/"
	cran = "assertr" 

	version("3.0.1", md5="b1aeebaf9ff6a7817c8e1759c2212275")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
