# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDf2yaml(RPackage):
	"""Convert Dataframe to 'YAML'

	The 'df2yaml' aims to simplify the process of converting 'dataframe' to 'YAML' <https://yaml.org/>. 
    The 'dataframe' with multiple key columns and one value column will be converted to the multi-level hierarchy.
	"""
	
	cran = "df2yaml" 

	version("0.3.1", md5="35319de48fed23cbbac9ae1abc221b10")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rrapply", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
