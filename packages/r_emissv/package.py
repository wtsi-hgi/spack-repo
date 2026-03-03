# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmissv(RPackage):
	"""Tools for Create Emissions for Air Quality Models

	Processing tools to create emissions for use in numerical air 
  quality models. Emissions can be calculated both using emission factors 
  and activity data (Schuch et al 2018) <doi:10.21105/joss.00662> or using 
  pollutant inventories (Schuch et al., 2018) <doi:10.30564/jasr.v1i1.347>. 
  Functions to process individual point emissions, line emissions and 
  area emissions of pollutants are available as well as methods to 
  incorporate alternative data for Spatial distribution of emissions 
  such as satellite images (Gavidia Calderon et. al, 2018) 
  <doi:10.1016/j.atmosenv.2018.09.026> or openstreetmap data 
  (Andrade et al, 2015) <doi:10.3389/fenvs.2015.00009>.
	"""
	
	homepage = "https://atmoschem.github.io/EmissV/"
	cran = "EmissV" 

	version("0.665.6.6", md5="35aef478616968e4deef1603007c6596")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-units@0.5.1:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
