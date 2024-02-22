# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGettddata(RPackage):
	"""Get Data for Brazilian Bonds (Tesouro Direto)

	Downloads and aggregates data for Brazilian government issued bonds directly from the website of Tesouro Direto <https://www.tesourodireto.com.br/>.
	"""
	
	homepage = "https://github.com/msperlin/GetTDData/"
	cran = "GetTDData" 

	version("1.5.4", md5="9152bb2edbe0b4aff71bb7555590b155")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-bizdays", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-humanize", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
