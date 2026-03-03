# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataresqc(RPackage):
	"""C3S Quality Control Tools for Historical Climate Data

	Quality control and formatting tools developed for the Copernicus Data Rescue Service. The package includes functions to handle the Station Exchange Format (SEF), various statistical tests for climate data at daily and sub-daily resolution, as well as functions to plot the data. For more information and documentation see <https://datarescue.climate.copernicus.eu/st_data-quality-control>.
	"""
	
	cran = "dataresqc" 

	version("1.1.1", md5="2416ffcbaeaac662683d0b63281ca2b9")

	depends_on("r@3.2:", type=("build", "run"))
