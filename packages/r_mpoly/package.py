# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpoly(RPackage):
	"""Symbolic Computation and More with Multivariate Polynomials

	Symbolic computing with multivariate polynomials in R.
	"""
	
	homepage = "https://github.com/dkahle/mpoly"
	cran = "mpoly" 

	version("1.1.1", md5="9eb7f1700c94ec815047e617e42602ab")

	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
