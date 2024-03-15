# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcdf4(RPackage):
	"""Interface to Unidata netCDF (Version 4 or Earlier) Format Data Files.

	Provides a high-level R interface to data files written using Unidata's
	netCDF library (version 4 or earlier), which are binary data files that are
	portable across platforms and include metadata information in addition to
	the data sets. Using this package, netCDF files (either version 4 or
	"classic" version 3) can be opened and data sets read in easily. It is also
	easy to create new netCDF dimensions, variables, and files, in either
	version 3 or 4 format, and manipulate existing netCDF files. This package
	replaces the former ncdf package, which only worked with netcdf version 3
	files. For various reasons the names of the functions have had to be
	changed from the names in the ncdf package. The old ncdf package is still
	available at the URL given below, if you need to have backward
	compatibility. It should be possible to have both the ncdf and ncdf4
	packages installed simultaneously without a problem. However, the ncdf
	package does not provide an interface for netcdf version 4 files."""

	cran = "ncdf4"

	license("GPL-3.0-or-later")

	version("1.22", md5="cdfddec28e78da74ed216052d469a585", url="https://cran.r-project.org/src/contrib/ncdf4_1.22.tar.gz")

	depends_on("netcdf-c@4.1:", type=("build", "link", "run"))
