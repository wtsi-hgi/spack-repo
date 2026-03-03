# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolytrend(RPackage):
	"""Trend Classification Algorithm

	This algorithm classifies the trends into linear, quadratic, cubic, concealed and no-trend types. The "concealed trends" are those trends that possess quadratic or cubic forms, but the net change from the start of the time period to the end of the time period hasn't been significant. The "no-trend" category includes simple linear trends with statistically in-significant slope coefficient.
	"""
	
	cran = "PolyTrend" 

	version("1.2", md5="d2acf7c599415917d131bd86ea25e04b")

