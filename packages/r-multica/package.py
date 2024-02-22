# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultica(RPackage):
	"""Multinomial Cochran-Armitage Trend Test

	Implements a generalization of the Cochran-Armitage trend test to
    multinomial data. In addition to an overall test, multiple testing adjusted
    p-values for trend in individual outcomes and power calculation is
    available.
	"""
	
	cran = "multiCA" 

	version("1.1", md5="078373297e0736e9f6053b03276dcaa7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
