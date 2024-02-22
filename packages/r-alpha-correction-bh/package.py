# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphaCorrectionBh(RPackage):
	"""Benjamini-Hochberg Alpha Correction

	Provides the alpha-adjustment correction from "Benjamini, Y., & Hochberg, Y. (1995) <doi:10.1111/j.2517-6161.1995.tb02031.x> Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal statistical society: series B (Methodological), 57(1), 289-300". For researchers interested in using the exact mathematical formulas and procedures as used in the original paper.
	"""
	
	cran = "alpha.correction.bh" 

	version("0.0.1", md5="3bc850f558afa4d006f0c299c3e99287")

	depends_on("r-knitr", type=("build", "run"))
