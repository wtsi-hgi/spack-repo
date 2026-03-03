# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLacrmr(RPackage):
	"""Connect to the 'Less Annoying CRM' API

	Connect to the 'Less Annoying CRM' API with ease to get your crm data in a clean and tidy format. 'Less Annoying CRM' is a simple CRM built for small businesses, more information is available on their website <https://www.lessannoyingcrm.com/>.
	"""
	
	homepage = "https://ixpantia.github.io/lacrmr/"
	cran = "lacrmr" 

	version("1.0.5", md5="b0e3c4b433eb6a40e391451c76ae4d1a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
