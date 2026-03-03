# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesbio(RPackage):
	"""Miscellaneous Functions for Bioinformatics and Bayesian
Statistics

	A hodgepodge of hopefully helpful functions. Two of these perform
    shrinkage estimation: one using a simple weighted method where the user can
    specify the degree of shrinkage required, and one using James-Stein shrinkage
    estimation for the case of unequal variances.
	"""
	
	cran = "bayesbio" 

	version("1.0.0", md5="389952250915e7d695c3dafb6bda0db5")

	depends_on("r@3.2:", type=("build", "run"))
