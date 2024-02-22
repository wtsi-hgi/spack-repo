# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBe(RPackage):
	"""Bioequivalence Study Data Analysis

	Analyze bioequivalence study data with industrial strength. Sample size could be determined for various crossover designs, such as 2x2 design, 2x4 design, 4x4 design, Balaam design, Two-sequence dual design, and William design.
             Reference: Chow SC, Liu JP. Design and Analysis of Bioavailability and Bioequivalence Studies. 3rd ed. (2009, ISBN:978-1-58488-668-6).
	"""
	
	homepage = "https://cran.r-project.org/package=BE"
	cran = "BE" 

	version("0.2.4", md5="7fcf11d4eba382a1b03549506d7ef6ea")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rtf", type=("build", "run"))
