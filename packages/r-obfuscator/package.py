# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObfuscator(RPackage):
	"""Obfuscation Game Designs

	When people make decisions, they may do so using a wide variety of decision rules. The package allows users to easily create obfuscation games to test the obfuscation hypothesis. It provides an easy to use interface and multiple options designed to vary the difficulty of the game and tailor it to the user's needs. For more detail: Chorus et al., 2021, Obfuscation maximization-based decision-making: Theory, methodology and first empirical evidence, Mathematical Social Sciences, 109, 28-44, <doi:10.1016/j.mathsocsci.2020.10.002>. 
	"""
	
	homepage = "https://obfuscator.edsandorf.me"
	cran = "obfuscatoR" 

	version("0.2.2", md5="b7d24e3f4cd1930ab224e2a018ee0195")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
