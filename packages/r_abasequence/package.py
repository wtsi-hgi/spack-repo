# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbasequence(RPackage):
	"""Coding 'ABA' Patterns for Sequence Data

	Provides a suite of functions for analyzing sequences of events. Users can generate and code sequences based on predefined rules, with a special focus on the identification of sequences coded as 'ABA' (when one element appears, followed by a different one, and then followed by the first). Additionally, the package offers the ability to calculate the length of consecutive 'ABA'-coded sequences sharing common elements. The methods implemented in this package are based on the work by Ziembowicz, K., Rychwalska, A., & Nowak, A. (2022). <doi:10.1177/10464964221118674>.
	"""
	
	cran = "abasequence" 

	version("0.1.0", md5="1392d909eb0f65be94fd4160a371ae21")

