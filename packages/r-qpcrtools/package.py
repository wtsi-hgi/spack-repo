# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpcrtools(RPackage):
	"""Tools for qPCR

	PKG_DESC.
	"""
	
	homepage = "https://github.com/lixiang117423/qPCRtools"
	cran = "qPCRtools" 

	version("1.0.1", md5="6d98c683c0c2577de19dd2f2823991ff")

	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
