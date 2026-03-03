# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmst(RPackage):
	"""Computerized Adaptive Multistage Testing

	Assemble the panels of computerized adaptive multistage testing by the 
    bottom-up and the top-down approach, and simulate the administration of the assembled 
    panels. The full documentation and tutorials are at <https://github.com/xluo11/Rmst>.
    Reference: Luo and Kim (2018) <doi:10.1111/jedm.12174>.
	"""
	
	homepage = "https://github.com/xluo11/Rmst"
	cran = "Rmst" 

	version("0.0.3", md5="f223184fbddc2714dc47b3bcc6784e6d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rata", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rirt", type=("build", "run"))
