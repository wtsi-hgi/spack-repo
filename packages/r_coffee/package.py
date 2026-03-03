# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoffee(RPackage):
	"""Chronological Ordering for Fossils and Environmental Events

	While individual calibrated radiocarbon dates can span several centuries, combining multiple dates together with any chronological constraints can make a chronology much more robust and precise. This package uses Bayesian methods to enforce the chronological ordering of radiocarbon and other dates, for example for trees with multiple radiocarbon dates spaced at exactly known intervals (e.g., 10 annual rings). For methods see Christen 2003 <doi:10.11141/ia.13.2>. Another example is sites where the relative chronological position of the dates is taken into account - the ages of dates further down a site must be older than those of dates further up (Buck, Kenworthy, Litton and Smith 1991 <doi:10.1017/S0003598X00080534>; Nicholls and Jones 2001 <doi:10.1111/1467-9876.00250>).
	"""
	
	homepage = "https://github.com/Maarten14C/coffee"
	cran = "coffee" 

	version("0.3.0", md5="b93c000aad43934e7d6ce448b24e5e58")

	depends_on("r-rintcal@0.6.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
