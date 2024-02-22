# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetdfpdata(RPackage):
	"""Reading Annual Financial Reports from Bovespa's DFP, FRE and FCA
System

	Reads annual financial reports including assets, liabilities, dividends history, stockholder composition and much more from Bovespa's DFP, FRE and FCA systems <http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm>.
 These are web based interfaces for all financial reports of companies traded at Bovespa. The package is specially designed for large scale data importation, keeping a tabular (long) structure for easier processing.  
	"""
	
	homepage = "https://github.com/msperlin/GetDFPData/"
	cran = "GetDFPData" 

	version("1.6", md5="a3a81c1fe01d36b893ab94e02fcc582b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
