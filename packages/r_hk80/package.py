# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHk80(RPackage):
	"""Conversion Tools for HK80 Geographical Coordinate System

	This is a collection of functions for converting coordinates between WGS84UTM, WGS84GEO, HK80UTM, HK80GEO and HK1980GRID Coordinate Systems used in Hong Kong SAR, based on the algorithms described in Explanatory Notes on Geodetic Datums in Hong Kong by Survey and Mapping Office Lands Department, Hong Kong Government (1995).
	"""
	
	homepage = "https://github.com/helixcn/"
	cran = "HK80" 

	version("0.0.2", md5="71488d2d14b7a82e94b9e6f2602bf0f4", url="https://cran.r-project.org/src/contrib/HK80_0.0.2.tar.gz")

