# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcesimfit(RPackage):
	"""ACE Kin Pair Data Simulations and Model Fitting

	A few functions aim to provide a statistic tool for three purposes. First, simulate kin pairs data based on the assumption that every trait is affected by genetic effects (A), common environmental effects (C) and unique environmental effects (E).Second, use kin pairs data to fit an ACE model and get model fit output.Third, calculate power of A estimate given a specific condition. For the mechanisms of power calculation, we suggest to check Visscher(2004)<doi:10.1375/twin.7.5.505>.
	"""
	
	cran = "ACEsimFit" 

	version("0.0.0.9", md5="ea405c47e08d6cb3cf2f4c9232cb026b")

	depends_on("r-openmx@2.19.6:", type=("build", "run"))
