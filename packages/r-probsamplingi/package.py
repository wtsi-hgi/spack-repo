# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbsamplingi(RPackage):
	"""Probabilistic Sampling Design and Strategies

	It allows the user to determine sample sizes, select probabilistic samples,
 make estimates of different parameters for the total finite population and in studio domains,
 using the main design drawings.
	"""
	
	cran = "ProbSamplingI" 

	version("2.0", md5="d0dc7dbf5637432309cee619603a9fed")

