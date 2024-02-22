# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoveldistns(RPackage):
	"""Computes PDF, CDF, Quantile, Random Numbers and Measures of
Inference for 3 General Families of Distributions

	Computes the probability density function, the cumulative density function, quantile function, random numbers and measures of inference for the following families exponentiated generalized gull alpha power family, exponentiated gull alpha powerfamily, gull alpha power family.
	"""
	
	cran = "NovelDistns" 

	version("0.1.0", md5="64ac9c8ac2a310fded92c2eff318406e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-adequacymodel", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
