# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeriscope(RPackage):
	"""Enterprise Streamlined 'Shiny' Application Framework

	An enterprise-targeted scalable and UI-standardized 'shiny' framework 
    including a variety of developer convenience functions with the goal of both 
    streamlining robust application development while assisting with creating a 
    consistent user experience regardless of application or developer.
	"""
	
	homepage = "https://github.com/cb4ds/periscope"
	cran = "periscope" 

	version("1.0.4", md5="d8f89447093ebb158311665ba3eefc4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinydashboard@0.5:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-writexl@1.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-fresh", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
