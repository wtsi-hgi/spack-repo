# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRipc(RPackage):
	"""Download and Tidy IPC and CH Data

	Utilities to access Integrated Food Security Phase Classification
    (IPC) and Cadre Harmonisé (CH) food security data. Wrapper functions are
    available for all of the 'IPC-CH' Public API (<https://docs.api.ipcinfo.org>)
    simplified and advanced endpoints to easily download the data in a clean and
    tidy format.
	"""
	
	homepage = "https://github.com/ocha-dap/ripc"
	cran = "ripc" 

	version("0.2.0", md5="b256b82f069b08939244a7a788ffac01")

	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
