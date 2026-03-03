# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAttrib(RPackage):
	"""Attributable Burden of Disease

	Provides functions for estimating the attributable burden of disease due to risk factors. The posterior simulation is performed using arm::sim as described in Gelman, Hill (2012) <doi:10.1017/CBO9780511790942> and the attributable burden method is based on Nielsen, Krause, Molbak <doi:10.1111/irv.12564>.
	"""
	
	cran = "attrib" 

	version("2021.1.2", md5="286f081ecbb07de5d0224c53c39f5355")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pbs", type=("build", "run"))
	depends_on("r-dlnm", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mvmeta", type=("build", "run"))
	depends_on("r-tsmodel", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
