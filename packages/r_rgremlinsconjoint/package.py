# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgremlinsconjoint(RPackage):
	"""Estimate the "Gremlins in the Data" Model for Conjoint Studies

	The tools and utilities to estimate the model described in "Gremlin's in the
    Data: Identifying the Information Content of Research Subjects" (Howell et al.
    (2021) <doi:10.1177/0022243720965930>)  using conjoint analysis data such as
    that collected in Sawtooth Software's 'Lighthouse' or 'Discover' products.
    Additional utilities are included for formatting the input data.
	"""
	
	homepage = "https://github.com/statuser/RGremlinsConjoint"
	cran = "RGremlinsConjoint" 

	version("0.9.1", md5="d4a2b4e13272fe6e41d074a512452d02")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bayesm", type=("build", "run"))
