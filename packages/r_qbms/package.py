# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQbms(RPackage):
	"""Query the Breeding Management System(s)

	This R package assists breeders in linking data systems with their analytic pipelines, 
    a crucial step in digitizing breeding processes. It supports querying and retrieving 
    phenotypic and genotypic data from systems like 'EBS' <https://ebs.excellenceinbreeding.org/>, 
    'BMS' <https://bmspro.io>, 'BreedBase' <https://breedbase.org>, and 
    'GIGWA' <https://github.com/SouthGreenPlatform/Gigwa2> (using 'BrAPI' <https://brapi.org> calls). 
    Extra helper functions support environmental data sources, including 
    'TerraClimate' <https://www.climatologylab.org/terraclimate.html> and 'FAO' 
    'HWSDv2' <https://gaez.fao.org/pages/hwsd> soil database. 
	"""
	
	homepage = "https://icarda-git.github.io/QBMS/"
	cran = "QBMS" 

	version("1.0.0", md5="8929b076af220deed7f7fc08e3132270")
	version("0.9.1", md5="28ad24c9d9bd4dbd1835e6a3670e3afa")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rnetcdf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
