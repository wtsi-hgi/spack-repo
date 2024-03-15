# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdalutilities(RPackage):
	"""Wrappers for 'GDAL' Utilities Executables.

	R's 'sf' package ships with self-contained 'GDAL' executables, including a
	bare bones interface to several 'GDAL'-related utility programs
	collectively known as the 'GDAL utilities'. For each of those utilities,
	this package provides an R wrapper whose formal arguments closely mirror
	those of the 'GDAL' command line interface. The utilities operate on data
	stored in files and typically write their output to other files. Therefore,
	to process data stored in any of R's more common spatial formats (i.e.
	those supported by the 'sp', 'sf', and 'raster' packages), first write them
	to disk, then process them with the package's wrapper functions before
	reading the outputted results back into R. GDAL function arguments
	introduced in GDAL version 3.2.1 or earlier are supported."""

	cran = "gdalUtilities"

	version("1.2.5", md5="dea827cf5ed9358a68e47667ac943fbc")

	depends_on("r-sf@1.0.11:", type=("build", "run"))
