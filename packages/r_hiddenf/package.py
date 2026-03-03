# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiddenf(RPackage):
	"""The All-Configurations, Maximum-Interaction F-Test for Hidden
Additivity

	Computes the ACMIF test and Bonferroni-adjusted p-value of interaction in two-factor studies.  Produces corresponding interaction plot and analysis of variance tables and p-values from several other tests of non-additivity.
	"""
	
	cran = "hiddenf" 

	version("2.0", md5="463cdff2acfdf55312c2379b50d0db26")

