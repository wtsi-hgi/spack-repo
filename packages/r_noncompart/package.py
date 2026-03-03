# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoncompart(RPackage):
	"""Noncompartmental Analysis for Pharmacokinetic Data

	Conduct a noncompartmental analysis with industrial strength.
             Some features are
             1) Use of CDISC SDTM terms
             2) Automatic or manual slope selection
             3) Supporting both 'linear-up linear-down' and 'linear-up log-down' method
             4) Interval(partial) AUCs with 'linear' or 'log' interpolation method
             * Reference: Gabrielsson J, Weiner D. Pharmacokinetic and Pharmacodynamic Data Analysis - Concepts and Applications. 5th ed. 2016. (ISBN:9198299107).
	"""
	
	homepage = "https://cran.r-project.org/package=NonCompart"
	cran = "NonCompart" 

	version("0.7.0", md5="37c61df5b854a134be36f94500121247")

