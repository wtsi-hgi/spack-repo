# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcop(RPackage):
	"""Simulate from Arbitrary Copulae

	Provides a framework to generating random variates from
             arbitrary multivariate copulae, while concentrating on
             (bivariate) extreme value copulae.  Particularly useful if
             the multivariate copulae are not available in closed
             form.   
	"""
	
	cran = "SimCop" 

	version("0.7.0", md5="85ce6375cd1137b68e0e9956570eea42")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
