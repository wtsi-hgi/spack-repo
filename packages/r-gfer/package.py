# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfer(RPackage):
	"""Green Finance and Environmental Risk

	Focuses on data collecting, analyzing and visualization in green finance and environmental 
  risk research and analysis. Main function includes environmental data collecting from 
  official websites such as MEP (Ministry of Environmental Protection of China, <https://www.mee.gov.cn>), water 
  related projects identification and environmental data visualization.
	"""
	
	homepage = "https://yuanchao-xu.github.io/gfer/"
	cran = "gfer" 

	version("0.1.12", md5="c435d0f7bb59731d363c14bbaf100980")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scatterpie", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-googlesheets4", type=("build", "run"))
	depends_on("r-gsheet", type=("build", "run"))
