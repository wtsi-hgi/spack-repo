# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REixport(RPackage):
	"""Export Emissions to Atmospheric Models

	Emissions are the mass of pollutants released into the atmosphere. Air quality models need emissions data, with spatial and temporal distribution, to represent air pollutant concentrations. This package, eixport, creates inputs for the air quality models 'WRF-Chem' Grell et al (2005) <doi:10.1016/j.atmosenv.2005.04.027>, 'MUNICH' Kim et al (2018) <doi:10.5194/gmd-11-611-2018> , 'BRAMS-SPM' Freitas et al (2005) <doi:10.1016/j.atmosenv.2005.07.017> and 'RLINE' Snyder et al (2013) <doi:10.1016/j.atmosenv.2013.05.074>. See the 'eixport' website (<https://atmoschem.github.io/eixport/>) for more information, documentations and examples. More details in Ibarra-Espinosa et al (2018) <doi:10.21105/joss.00607>.
	"""
	
	homepage = "https://atmoschem.github.io/eixport/"
	cran = "eixport" 

	version("0.6.0", md5="a02f4a4b181329e267cdf162aa01fcc6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-cptcity", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
