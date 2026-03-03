# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmkdiscrete(RPackage):
	"""Sundry Discrete Probability Distributions

	Sundry discrete probability distributions and helper functions.
	"""
	
	cran = "RMKdiscrete" 

	version("0.2", md5="0b33172b207db83266404dad642d09d0")

	depends_on("r@2.15:", type=("build", "run"))
