# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetdfpdata2(RPackage):
	"""Reading Annual and Quarterly Financial Reports from B3

	Reads annual and quarterly financial reports from companies traded at B3, the Brazilian exchange 
            <https://www.b3.com.br/>. 
            All data is downloaded and imported from CVM's public ftp site <https://dados.cvm.gov.br/dados/CIA_ABERTA/>.
	"""
	
	homepage = "https://github.com/msperlin/GetDFPData2/"
	cran = "GetDFPData2" 

	version("0.6.3", md5="406259309f95e79a2e65dc55be9ffb09", url="https://cran.r-project.org/src/contrib/GetDFPData2_0.6.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
