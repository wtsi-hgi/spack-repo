# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsvr(RPackage):
	"""Timescale-Specific Variance Ratio for Use in Community Ecology

	Tools for timescale decomposition of the classic variance ratio of community ecology. Tools are as described in Zhao et al (in prep), extending commonly used methods introduced by Peterson et al (1975) <doi: 10.2307/1936306>.
	"""
	
	cran = "tsvr" 

	version("1.0.2", md5="516876551e6b894a82f3483f5355b790")

