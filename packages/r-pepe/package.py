# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepe(RPackage):
	"""Data Manipulation

	Is designed to make easier printing summary statistics (for continues and factor level) tables in Latex, and plotting by factor. 
	"""
	
	homepage = "https://github.com/seymakalay/pepe"
	cran = "pepe" 

	version("1.2.0", md5="15d543064baaf665793d25e211f169e3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
