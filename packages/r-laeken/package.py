# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLaeken(RPackage):
	"""Estimation of Indicators on Social Exclusion and Poverty

	Estimation of indicators on social exclusion and poverty, as well
    as Pareto tail modeling for empirical income distributions.
	"""
	
	cran = "laeken" 

	version("0.5.3", md5="53ce6fcbfb5e1ba2ecaafa353665bbaf")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
