# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsafishercombined(RPackage):
	"""Gene Set Analysis with Fisher Combined Method

	Provides the p-value for a joint test of association between a phenotype and a set of genetic variants (SNPs) by combining marginal p-values using the Fisher method. See Fisher, R.A. (1925,ISBN:0-05-002170-2) Statistical Methods for Research Workers.
	"""
	
	cran = "GSAfisherCombined" 

	version("1.0", md5="4fa3c1f780fa99604746216528985ad9")

