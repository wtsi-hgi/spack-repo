# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcar(RPackage):
	"""Noncompartmental Analysis for Pharmacokinetic Report

	Conduct a noncompartmental analysis with industrial strength.
             Some features are
             1) CDISC SDTM terms
             2) Automatic or manual slope selection
             3) Supporting both 'linear-up linear-down' and 'linear-up log-down' method
             4) Interval(partial) AUCs with 'linear' or 'log' interpolation method
             5) Produce pdf, rtf, text report files.
             * Reference: Gabrielsson J, Weiner D. Pharmacokinetic and Pharmacodynamic Data Analysis - Concepts and Applications. 5th ed. 2016. (ISBN:9198299107).
	"""
	
	homepage = "https://cran.r-project.org/package=ncar"
	cran = "ncar" 

	version("0.5.0", md5="88996b6d260d80e1cf5d28768676ff5e")

	depends_on("r-rtf", type=("build", "run"))
	depends_on("r-noncompart@0.7:", type=("build", "run"))
