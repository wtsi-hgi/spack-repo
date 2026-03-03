# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazeinda(RPackage):
	"""Monotonic Association on Zero-Inflated Data

	Methods for calculating and testing the significance of
  pairwise monotonic association from and based on the work of
  Pimentel (2009) <doi:10.4135/9781412985291.n2>. Computation of association of vectors from one
  or multiple sets can be performed in parallel thanks to the
  packages 'foreach' and 'doMC'.
	"""
	
	cran = "mazeinda" 

	version("0.0.2", md5="e7d5dd5e84426a6a298c4fce717362b1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
