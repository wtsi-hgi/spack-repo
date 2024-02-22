# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStockanalyst(RPackage):
	"""Equity Valuation using Methods of Fundamental Analysis

	Methods of Fundamental Analysis for Valuation of Equity included here serve as a quick reference for undergraduate courses on Stock Valuation and Chartered Financial Analyst Levels 1 and 2 Readings on Equity Valuation.
    Jerald E. Pinto (“Equity Asset Valuation (4th Edition)”, 2020, ISBN: 9781119628194).
    Chartered Financial Analyst Institute ("Chartered Financial Analyst Program Curriculum 2020 Level I Volumes 1-6. (Vol. 4, pp. 445-491)", 2019, ISBN: 9781119593577).
    Chartered Financial Analyst Institute ("Chartered Financial Analyst Program Curriculum 2020 Level II Volumes 1-6. (Vol. 4, pp. 197-447)", 2019, ISBN: 9781119593614).
	"""
	
	cran = "stockAnalyst" 

	version("1.0.1", md5="cb8a1d6883d4dafe1287b17d79ab0276")

