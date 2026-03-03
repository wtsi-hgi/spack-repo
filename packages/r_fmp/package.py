# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmp(RPackage):
	"""Filtered Monotonic Polynomial IRT Models

	Estimates Filtered Monotonic Polynomial IRT Models as described by Liang and Browne (2015) <DOI:10.3102/1076998614556816>. 
	"""
	
	cran = "FMP" 

	version("1.4", md5="e20b0ba3554f3d90c22218984ccff78c")

	depends_on("r@3:", type=("build", "run"))
