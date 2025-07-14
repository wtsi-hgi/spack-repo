# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStategra(RPackage):
	"""Classes and methods for multi-omics data integration

	Classes and tools for multi-omics data integration.
	"""
	
	bioc = "STATegRa"

	version("1.44.0", commit="8763e591d2b4374d5921ca3a4115d82ede93be3b")
	version("1.38.0", commit="fe2962b7c4098361fc0a0847957581bfc0bdb733")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
