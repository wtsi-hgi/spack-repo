# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBusinessplanr(RPackage):
	"""Simple Modelling Tools for Business Plans

	A collection of S4 classes, methods and functions to create
        and visualize business plans. Different types of cash flows can be
        defined, which can then be used and tabulated to create profit and
        loss statements, cash flow plans, investment and depreciation
        schedules, loan amortization schedules, etc. The methods are
        designed to produce handsome tables in both PDF and HTML using
        'RMarkdown' or 'Shiny'.
	"""
	
	homepage = "https://www.c3s.cc"
	cran = "businessPlanR" 

	version("0.1-0", md5="4d94a6ccbb891d6de00ee95e568d0988")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
