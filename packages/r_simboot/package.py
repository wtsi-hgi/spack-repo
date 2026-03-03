# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimboot(RPackage):
	"""Simultaneous Inference for Diversity Indices

	Provides estimation of simultaneous bootstrap and asymptotic confidence intervals for diversity indices, namely the Shannon and the Simpson index. Several pre--specified multiple comparison types are available to choose. Further user--defined contrast matrices are applicable. In addition, simboot estimates adjusted as well as unadjusted p--values for two of the three proposed bootstrap methods. Further simboot allows for comparing biological diversities of two or more groups while simultaneously testing a user-defined selection of Hill numbers of orders q, which are considered as appropriate and useful indices for measuring diversity.
	"""
	
	homepage = "https://github.com/shearer/simboot"
	cran = "simboot" 

	version("0.2-8", md5="436ca40d374e14b049f770f6baaf1105")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
