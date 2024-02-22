# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvar(RPackage):
	"""Compute Expected Shortfall and Value at Risk for Continuous
Distributions

	Compute expected shortfall (ES) and Value at Risk (VaR) from a
    quantile function, distribution function, random number generator or
    probability density function.  ES is also known as Conditional Value at
    Risk (CVaR). Virtually any continuous distribution can be specified.
    The functions are vectorized over the arguments. The computations are
    done directly from the definitions, see e.g. Acerbi and Tasche (2002)
    <doi:10.1111/1468-0300.00091>. Some support for GARCH models is provided,
    as well.
	"""
	
	homepage = "https://geobosh.github.io/cvar/"
	cran = "cvar" 

	version("0.5", md5="ed649d29f7a380f83ff51d24512a34a0")

	depends_on("r-gbutils", type=("build", "run"))
	depends_on("r-rdpack@0.8:", type=("build", "run"))
