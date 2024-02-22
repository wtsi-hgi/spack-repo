# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMchtest(RPackage):
	"""Monte Carlo Hypothesis Tests with Sequential Stopping

	Performs Monte Carlo hypothesis tests, allowing a couple of different sequential stopping boundaries. For example, a truncated sequential probability ratio test boundary (Fay, Kim and Hachey, 2007 <DOI:10.1198/106186007X257025>) and a boundary proposed by Besag and Clifford, 1991 <DOI:10.1093/biomet/78.2.301>. Gives valid p-values and confidence intervals on p-values.
	"""
	
	homepage = "https://www.niaid.nih.gov/about/brb-staff-fay"
	cran = "MChtest" 

	version("1.0-3", md5="792cbd7d74c6ebc9478b4c2657328079")

