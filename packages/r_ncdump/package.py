# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcdump(RPackage):
	"""Extract Metadata from 'NetCDF' Files as Data Frames

	Tools for handling 'NetCDF' metadata in data frames. The metadata is provided
    as relations in tabular form, to avoid having to scan printed header output or to navigate 
    nested lists of raw metadata. 
	"""
	
	homepage = "https://github.com/r-gris/ncdump"
	cran = "ncdump" 

	version("0.0.3", md5="d472d47eb6cce5407a6034957d180102")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
