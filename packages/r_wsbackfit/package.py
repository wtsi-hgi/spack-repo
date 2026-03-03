# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWsbackfit(RPackage):
	"""Weighted Smooth Backfitting for Structured Models

	Non- and semiparametric regression for generalized additive, partial linear, and varying coefficient models as well as their combinations via smoothed backfitting. Based on Roca-Pardinas J and Sperlich S (2010) <doi:10.1007/s11222-009-9130-2>; Mammen E, Linton O and Nielsen J (1999) <doi:10.1214/aos/1017939138>; Lee YK, Mammen E, Park BU (2012) <doi:10.1214/12-AOS1026>.
	"""
	
	cran = "wsbackfit" 

	version("1.0-5", md5="2fcaa0cb926ce58b8190c65bb18d154f")

	depends_on("r@3.5:", type=("build", "run"))
