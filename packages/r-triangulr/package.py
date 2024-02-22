# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriangulr(RPackage):
	"""High-Performance Triangular Distribution Functions

	A collection of high-performance functions for the triangular
    distribution that consists of the probability density function, cumulative
    distribution function, quantile function, random variate generator, moment
    generating function, characteristic function, and expected shortfall
    function. References: Samuel Kotz, Johan Ren Van Dorp (2004)
    <doi:10.1142/5720> and Acerbi, Carlo and Tasche, Dirk. (2002)
    <doi:10.1111/1468-0300.00091>.
	"""
	
	homepage = "https://github.com/irkaal/triangulr/"
	cran = "triangulr" 

	version("1.2.1", md5="d9d392dc81ab2b0b23231bc01fb0771f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-vctrs@0.3.8:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
