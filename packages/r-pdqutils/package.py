# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdqutils(RPackage):
	"""PDQ Functions via Gram Charlier, Edgeworth, and Cornish Fisher
Approximations

	A collection of tools for approximating the 'PDQ' functions
    (respectively, the cumulative distribution, density, and quantile) of
    probability distributions via classical expansions involving moments and
    cumulants.
	"""
	
	homepage = "https://github.com/shabbychef/PDQutils"
	cran = "PDQutils" 

	version("0.1.6", md5="c2606595a476eb1b44d8706f3c12032f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
