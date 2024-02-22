# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdrci(RPackage):
	"""Permutation-Based FDR Point and Confidence Interval Estimation

	FDR functions for permutation-based estimators, including pi0 as well as FDR
             confidence intervals. The confidence intervals account for dependencies between
             tests by the incorporation of an overdispersion parameter, which is estimated
             from the permuted data. Also included are options for an analog parametric approach.
	"""
	
	cran = "fdrci" 

	version("2.4", md5="7d472da26191830ae5ec70f2c85d8973")

	depends_on("r-ggplot2", type=("build", "run"))
