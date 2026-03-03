# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvcompare(RPackage):
	"""Compare Real Valued Random Variables

	A framework with tools to compare two random variables via stochastic dominance. See the README.md at <https://github.com/EtorArza/RVCompare> for a quick start guide. It can compute the Cp and Cd of two probability distributions and the Cumulative Difference Plot as explained in E. Arza (2022) <doi:10.1080/10618600.2022.2084405>. Uses bootstrap or DKW-bounds to compute the confidence bands of the cumulative distributions. These two methods are described in B. Efron. (1979) <doi:10.1214/aos/1176344552> and P. Massart (1990) <doi:10.1214/aop/1176990746>.
	"""
	
	cran = "RVCompare" 

	version("0.1.8", md5="148f95785384c33c50c5f9825511fcab")

	depends_on("r-pracma@2.2.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
