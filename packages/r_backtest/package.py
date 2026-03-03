# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacktest(RPackage):
	"""Exploring Portfolio-Based Conjectures About Financial
Instruments

	The backtest package provides facilities for exploring
        portfolio-based conjectures about financial instruments
        (stocks, bonds, swaps, options, et cetera).
	"""
	
	cran = "backtest" 

	version("0.3-4", md5="0e15d0b071d352ecdc6efea8adb2d7ba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
