# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrvyr(RPackage):
	"""'dplyr'-Like Syntax for Summary Statistics of Survey Data

	Use piping, verbs like 'group_by' and 'summarize', and other
    'dplyr' inspired syntactic style when calculating summary statistics on survey
    data using functions from the 'survey' package.
	"""
	
	homepage = "http://gdfe.co/srvyr/"
	cran = "srvyr" 

	version("1.2.0", md5="2a12395b8093e17af3db304d328648bd")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survey@4.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
