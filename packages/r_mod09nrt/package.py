# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMod09nrt(RPackage):
	"""Extraction of Bands from MODIS Surface Reflectance Product MOD09
NRT

	Package for processing downloaded MODIS Surface reflectance
    Product HDF files. Specifically, MOD09 surface reflectance product files, and
    the associated MOD03 geolocation files (for MODIS-TERRA). The package will be
    most effective if the user installs MRTSwath (MODIS Reprojection Tool for swath
    products; <https://lpdaac.usgs.gov/tools/modis_reprojection_tool_swath>, and
    adds the directory with the MRTSwath executable to the default R PATH by editing
    ~/.Rprofile.
	"""
	
	cran = "mod09nrt" 

	version("0.14", md5="2cd9640e01490c5b4481847a56e81368")

