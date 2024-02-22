# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubts(RPackage):
	"""Positive Tempered Stable Distributions and Related Subordinators

	Contains methods for the simulation of positive tempered stable distributions and related subordinators. Including classical tempered stable, rapidly deceasing tempered stable, truncated stable, truncated tempered stable, generalized Dickman, truncated gamma, generalized gamma, and p-gamma. For details, see Dassios et al (2019) <doi:10.1017/jpr.2019.6>, Dassios et al (2020) <doi:10.1145/3368088>, Grabchak (2021) <doi:10.1016/j.spl.2020.109015>.
	"""
	
	cran = "SubTS" 

	version("1.0", md5="0cfe6b8676e2d3eed4d0f00a9d9f6bdc")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-tweedie", type=("build", "run"))
