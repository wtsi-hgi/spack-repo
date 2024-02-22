# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRplum(RPackage):
	"""Bayesian Age-Depth Modelling of Cores Dated by Pb-210

	An approach to age-depth modelling that uses Bayesian statistics to reconstruct accumulation histories for 210Pb-dated deposits using prior information. It can combine 210Pb, radiocarbon, and other dates in the chronologies. See Aquino et al. (2018) <doi:10.1007/s13253-018-0328-7>. Note that parts of the code underlying 'rplum' are derived from the 'rbacon' package by the same authors, and there remains a degree of overlap between the two packages.
	"""
	
	cran = "rplum" 

	version("0.4.0", md5="a208e2aacf0253880ad33779e0b6b84f")

	depends_on("r-rbacon@3.2:", type=("build", "run"))
	depends_on("r-rintcal@0.6.4:", type=("build", "run"))
