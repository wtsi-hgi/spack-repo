# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCredsubs(RPackage):
	"""Credible Subsets

	Functions for constructing simultaneous credible bands and identifying subsets via the "credible subsets" (also called "credible subgroups") method. Package documentation includes the vignette included in this package, and the paper by Schnell, Fiecas, and Carlin (2020, <doi:10.18637/jss.v094.i07>).
	"""
	
	cran = "credsubs" 

	version("1.1.1", md5="04bf7399964576260b3521a9839490d3")

