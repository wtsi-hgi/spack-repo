# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeriscope2(RPackage):
	"""Enterprise Streamlined 'shiny' Application Framework Using
'bs4Dash'

	A framework for building enterprise, scalable and UI-standardized 'shiny' applications.  
    It brings enhanced features such as 'bootstrap' v4 <https://getbootstrap.com/docs/4.0/getting-started/introduction/>,
    additional and enhanced 'shiny' modules, customizable UI features, as well as an enhanced application file
    organization paradigm. This update allows developers to harness the ability to build powerful applications and 
    enriches the 'shiny' developers' experience when building and  maintaining applications.
	"""
	
	homepage = "https://github.com/Aggregate-Genius/periscope2"
	cran = "periscope2" 

	version("0.2.3", md5="2dd1cf144e6d794724271ed930a92e4e", url="https://cran.r-project.org/src/contrib/periscope2_0.2.3.tar.gz")
	version("0.2.2", md5="0f1b418577a64b805fa492f0683ece6f", url="https://cran.r-project.org/src/contrib/periscope2_0.2.2.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-bs4dash@2.3:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-fresh", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
