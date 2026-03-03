# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedas(RPackage):
	"""Companion Package to the Book 'R: Einführung durch angewandte
Statistik'

	Provides functions used in the 'R: Einführung durch angewandte Statistik' (second edition).
	"""
	
	cran = "REdaS" 

	version("0.9.4", md5="aeebd782a75972fdfa2a3f8d3cc82a99")

	depends_on("r@3:", type=("build", "run"))
