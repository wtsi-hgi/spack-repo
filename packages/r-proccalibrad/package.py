# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProccalibrad(RPackage):
	"""Extraction of Bands from MODIS Calibrated Radiances MOD02 NRT

	Package for processing downloaded MODIS Calibrated radiances
    Product HDF files. Specifically, MOD02 calibrated radiance product files, and
    the associated MOD03 geolocation files (for MODIS-TERRA). The package will be
    most effective if the user installs MRTSwath (MODIS Reprojection Tool for swath
    products; <https://lpdaac.usgs.gov/tools/modis_reprojection_tool_swath>, and
    adds the directory with the MRTSwath executable to the default R PATH by editing
    ~/.Rprofile.
	"""
	
	cran = "proccalibrad" 

	version("0.14", md5="e1de4baf7bd8c849d0460c90787ecf51")

