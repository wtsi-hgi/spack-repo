# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootcomb(RPackage):
	"""Combine Parameter Estimates via Parametric Bootstrap

	Propagate uncertainty from several estimates when combining these estimates via a function.
    This is done by using the parametric bootstrap to simulate values from the distribution of each estimate to build up an empirical distribution of the combined parameter.
    Finally either the percentile method is used or the highest density interval is chosen to derive a confidence interval for the combined parameter with the desired coverage.
    Gaussian copulas are used for when parameters are assumed to be dependent / correlated.
    References: Davison and Hinkley (1997,ISBN:0-521-57471-4) for the parametric bootstrap and percentile method, Gelman et al. (2014,ISBN:978-1-4398-4095-5) for the highest density interval, Stockdale et al. (2020)<doi:10.1016/j.jhep.2020.04.008> for an example of combining conditional prevalences.
	"""
	
	cran = "bootComb" 

	version("1.1.2", md5="a87707b3783895e6e787d047d0f6fc28")

	depends_on("r-mass@7.3.54:", type=("build", "run"))
