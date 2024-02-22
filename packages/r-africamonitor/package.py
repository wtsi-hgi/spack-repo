# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfricamonitor(RPackage):
	"""Africa Macroeconomic Monitor Database API

	An R API providing access to a relational database with macroeconomic data for Africa. 
             The database contains >700 macroeconomic time series from mostly international sources, 
             grouped into 50 macroeconomic and development-related topics. Series are carefully selected
             on the basis of data coverage for Africa, frequency, and relevance to the macro-development context. 
             The project is part of the 'Kiel Institute Africa Initiative' 
             <https://www.ifw-kiel.de/institute/initiatives/kiel-institute-africa-initiative/>, 
             which, amongst other things, aims to develop a parsimonious database with highly relevant indicators 
             to monitor macroeconomic developments in Africa, accessible through a fast API and a web-based platform
             at <https://africamonitor.ifw-kiel.de/>. 
             The database is maintained at the Kiel Institute for the World Economy <https://www.ifw-kiel.de/>. 
	"""
	
	homepage = "https://africamonitor.ifw-kiel.de/"
	cran = "africamonitor" 

	version("0.2.4", md5="5b4e72355687b875a11aa99d33dea617")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-collapse@2:", type=("build", "run"))
