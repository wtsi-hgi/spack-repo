# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlgebraichaplopackage(RPackage):
	"""Haplotype Two Snips Out of a Paired Group of Patients

	Two unordered pairs of data of two different snips positions is haplotyped by resolving a small number ob closed equations.
	"""
	
	cran = "AlgebraicHaploPackage" 

	version("1.2", md5="32ccb110f4b23c2810b830feee355bd1")

	depends_on("r@3.1.3:", type=("build", "run"))
