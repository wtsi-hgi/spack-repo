# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetfredata(RPackage):
	"""Reading FRE Corporate Data of Public Traded Companies from B3

	Reads corporate data such as board composition and compensation for companies traded at B3, 
             the Brazilian exchange <https://www.b3.com.br/>. All data is downloaded and imported from the ftp site <http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/FRE/>.
	"""
	
	homepage = "https://github.com/msperlin/GetFREData/"
	cran = "GetFREData" 

	version("0.8.1", md5="578fee6f35178eff4a3e7418dcc2ac20")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-getdfpdata2", type=("build", "run"))
