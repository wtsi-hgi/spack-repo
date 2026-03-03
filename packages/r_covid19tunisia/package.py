# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19tunisia(RPackage):
	"""Cases of COVID-19 in Tunisia

	Data personally collected about the spread of COVID-19 (SARS-COV-2) in Tunisia
    <https://github.com/MounaBelaid/covid19datatunisia>.
	"""
	
	homepage = "https://github.com/MounaBelaid/covid19tunisia"
	cran = "covid19tunisia" 

	version("0.1.0", md5="6d6543c89456eb71fbe70b114c8aec35")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-glue@1.3.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-knitr@1.7:", type=("build", "run"))
