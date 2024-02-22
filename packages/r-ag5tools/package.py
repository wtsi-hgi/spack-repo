# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAg5tools(RPackage):
	"""Toolbox for Downloading and Extracting Copernicus AgERA5 Data

	Tools for downloading and extracting data from the Copernicus "Agrometeorological indicators 
  from 1979 to present derived from reanalysis"
  <https://cds.climate.copernicus.eu/cdsapp#!/dataset/sis-agrometeorological-indicators?tab=overview> (AgERA5).
	"""
	
	homepage = "https://agrdatasci.github.io/ag5Tools/"
	cran = "ag5Tools" 

	version("0.0.2", md5="6a1c7889b84f7a4ac5681dfc3ffb4302")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
