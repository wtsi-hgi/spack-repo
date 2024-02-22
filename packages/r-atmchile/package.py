# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtmchile(RPackage):
	"""Download Air Quality and Meteorological Information of Chile

	Download air quality and meteorological information of Chile from  the National Air Quality System (S.I.N.C.A.)<https://sinca.mma.gob.cl/> dependent on the Ministry of the Environment and the Meteorological Directorate of Chile (D.M.C.)<http://www.meteochile.gob.cl/> dependent on the Directorate General of Civil Aeronautics.
	"""
	
	homepage = "https://github.com/franciscoxaxo/AtmChile"
	cran = "AtmChile" 

	version("1.0.1", md5="1842493b3639244bee74f8170b66d173")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
