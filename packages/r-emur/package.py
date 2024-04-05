# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmur(RPackage):
	"""Main Package of the EMU Speech Database Management System

	Provide the EMU Speech Database Management System (EMU-SDMS) with
    database management, data extraction, data preparation and data
    visualization facilities. See <https://ips-lmu.github.io/The-EMU-SDMS-Manual/>
    for more details.
	"""
	
	homepage = "https://github.com/IPS-LMU/emuR"
	cran = "emuR" 

	version("2.5.0", md5="b49e90324a34c92796776db0aca4433a")
	version("2.4.2", md5="119f8d234121e87707ad0a9b5fa68354")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-wrassp@0.1.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-rsqlite@2:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-httpuv@1.3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
	depends_on("r-mime@0.6:", type=("build", "run"))
	depends_on("r-rstudioapi@0.10:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-v8@3.4:", type=("build", "run"))
	depends_on("r-cli@2.5:", type=("build", "run"))
