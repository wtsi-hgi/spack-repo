# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAopdata(RPackage):
	"""Data from the 'Access to Opportunities Project (AOP)'

	Download data from the 'Access to Opportunities Project (AOP)'. The 
             'aopdata' package brings annual estimates of access to employment, 
             health, education and social assistance services by transport mode, 
             as well as data  on the spatial distribution of population, jobs, 
             health care, schools and social assistance facilities at a fine 
             spatial resolution for all cities included in the project. More 
             info on the 'AOP' website <https://www.ipea.gov.br/acessooportunidades/en/>.
	"""
	
	homepage = "https://github.com/ipeaGIT/aopdata"
	cran = "aopdata" 

	version("1.0.3", md5="956e120f2f75b38896988127137553d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-sf@0.9.3:", type=("build", "run"))
