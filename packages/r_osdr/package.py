# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsdr(RPackage):
	"""Finds an Optimal System of Distinct Representatives

	Provides routines for finding an Optimal System of Distinct Representatives (OSDR),
 as defined by D.Gale (1968) <doi:10.1016/S0021-9800(68)80039-0>.
	"""
	
	homepage = "https://cran.r-project.org/package=OSDR"
	cran = "OSDR" 

	version("1.1.4", md5="613354e3cd34be986b1dafe395542546")

