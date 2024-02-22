# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVein(RPackage):
	"""Vehicular Emissions Inventories

	Elaboration of vehicular emissions inventories,
    consisting in four stages, pre-processing activity data, preparing 
    emissions factors, estimating the emissions and post-processing of emissions 
    in maps and databases. More details in Ibarra-Espinosa et al (2018) <doi:10.5194/gmd-11-2209-2018>.
    Before using VEIN you need to know the vehicular composition of your study area, in other words,
    the combination of of type of vehicles, size and fuel of the fleet. Then, it is recommended to
    start with the project to download a template to create a structure of directories and scripts.
	"""
	
	homepage = "https://github.com/atmoschem/vein"
	cran = "vein" 

	version("1.0.2", md5="1aa828e8d062888782f836e8c2b1e288")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@1.0.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-dotcall64", type=("build", "run"))
	depends_on("r-cptcity", type=("build", "run"))
