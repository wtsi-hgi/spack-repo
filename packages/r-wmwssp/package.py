# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWmwssp(RPackage):
	"""Wilcoxon-Mann-Whitney Sample Size Planning

	Calculates the minimal sample size for the Wilcoxon-Mann-Whitney test
    that is needed for a given power and two sided type I error rate. The method works for metric data with and without
    ties, count data, ordered categorical data, and even dichotomous data.
    But data is needed for the reference group to generate synthetic data for the treatment group based on a relevant effect.
    For details, see Brunner, E., Bathke A. C. and Konietschke, F: Rank- and Pseudo-Rank Procedures in Factorial Designs - Using R and SAS, Springer Verlag, to appear.
	"""
	
	homepage = "http://github.com/happma/WMWssp"
	cran = "WMWssp" 

	version("0.4.0", md5="644f71ae196dc8471fb10f94cbe71558")

	depends_on("r@3.4:", type=("build", "run"))
