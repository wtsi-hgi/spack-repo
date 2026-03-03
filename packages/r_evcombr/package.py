# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvcombr(RPackage):
	"""Evidence Combination in R

	Combine pieces of evidence in the form of uncertainty representations.
	"""
	
	cran = "EvCombR" 

	version("0.1-4", md5="79d5c6d2fc985bb160018ba9716e61e0")

