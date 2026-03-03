# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkr(RPackage):
	"""Pharmacokinetics in R

	Conduct a noncompartmental analysis as closely as possible to the most widely used commercial software.
             Some features are
             1) CDISC SDTM terms
             2) Automatic slope selection with the same criterion of WinNonlin(R)
             3) Supporting both 'linear-up linear-down' and 'linear-up log-down' method
             4) Interval(partial) AUCs with 'linear' or 'log' interpolation method
             * Reference: Gabrielsson J, Weiner D. Pharmacokinetic and Pharmacodynamic Data Analysis - Concepts and Applications. 5th ed. 2016. (ISBN:9198299107).
	"""
	
	homepage = "https://cran.r-project.org/package=pkr"
	cran = "pkr" 

	version("0.1.3", md5="a4f107ed355763baccd1857bdeb83777")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-binr", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-rtf", type=("build", "run"))
