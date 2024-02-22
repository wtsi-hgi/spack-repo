# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdimpute(RPackage):
	"""A Batch Process for High Dimensional Imputation

	A correlation-based batch process for fast, accurate imputation for 
    high dimensional missing data problems via chained random forests.
    See Waggoner (2023) <doi:10.1007/s00180-023-01325-9> for more on 'hdImpute',
    Stekhoven and Bühlmann (2012) <doi:10.1093/bioinformatics/btr597> for more on 'missForest', 
    and Mayer (2022) <https://github.com/mayer79/missRanger> for more on 'missRanger'.
	"""
	
	homepage = "https://github.com/pdwaggoner/hdImpute"
	cran = "hdImpute" 

	version("0.2.1", md5="c0cc7147972cd1081979c372a36f87fc")

	depends_on("r-missranger", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
