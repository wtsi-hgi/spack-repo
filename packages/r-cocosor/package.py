# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocosor(RPackage):
	"""CoCoSo - Combined Compromise Solution Method for MCDA

	Provides a set of functions to implement the Combined Compromise Solution (CoCoSo) Method created by Yazdani, Zarate, Zavadskas and Turskis (2019) <doi:10.1108/MD-05-2017-0458>. This method is based on an integrated simple additive weighting and compromise exponentially weighted product model.
	"""
	
	cran = "cocosoR" 

	version("0.1.0", md5="f3dc13aa4f2e0b67373c7930d00f1b21")

	depends_on("r@2.10:", type=("build", "run"))
