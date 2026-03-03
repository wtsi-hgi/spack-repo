# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLorad(RPackage):
	"""Lowest Radial Distance Method of Marginal Likelihood Estimation

	Estimates marginal likelihood from a posterior sample using the method described in Wang et al. (2023) <doi:10.1093/sysbio/syad007>, which does not require evaluation of any additional points and requires only the log of the unnormalized posterior density for each sampled parameter vector.
	"""
	
	cran = "lorad" 

	version("0.0.1.0", md5="a8a88d53db1901039d7119432cc04d9d")

	depends_on("r@3:", type=("build", "run"))
