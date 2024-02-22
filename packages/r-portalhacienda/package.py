# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortalhacienda(RPackage):
	"""Acceder Con R a Los Datos Del Portal De Hacienda

	Obtener listado de datos, acceder y extender series del Portal de 
    Datos de Hacienda.Las proyecciones se realizan con 'forecast', 
    Hyndman RJ, Khandakar Y (2008) <doi:10.18637/jss.v027.i03>. 
    Search, download and forecast time-series from the Ministry of Economy 
    of Argentina. Forecasts are built with the 'forecast' package, 
    Hyndman RJ, Khandakar Y (2008) <doi:10.18637/jss.v027.i03>. 
	"""
	
	homepage = "https://github.com/fmgarciadiaz/PortalHacienda-CRAN"
	cran = "PortalHacienda" 

	version("0.1.7", md5="0618b82932a141be34c580c230f1c38d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-forecast@8.12:", type=("build", "run"))
	depends_on("r-timetk@2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.8:", type=("build", "run"))
	depends_on("r-xts@0.12.0:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-zoo@1.8.8:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
