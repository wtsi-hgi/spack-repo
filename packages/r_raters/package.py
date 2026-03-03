# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaters(RPackage):
	"""A Modification of Fleiss' Kappa in Case of Nominal and Ordinal
Variables

	The kappa statistic implemented by Fleiss is a very popular index for assessing the reliability of agreement among multiple observers. It is used both in the psychological and in the psychiatric field. Other fields of application are typically medicine, biology and engineering. Unfortunately,the kappa statistic may behave inconsistently in case of strong agreement between raters, since this index assumes lower values than it would have been expected. We propose a modification kappa implemented by Fleiss in case of nominal and ordinal variables. Monte Carlo simulations are used both to testing statistical hypotheses and to calculating percentile bootstrap confidence intervals based on proposed statistic in case of nominal and ordinal data.
	"""
	
	cran = "raters" 

	version("2.0.3", md5="968ad75f6bca7d38bfd8ec965287dfe3")

