# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoupx(RPackage):
	"""Single Cell mRNA Soup eXterminator

	Quantify, profile and remove ambient mRNA contamination (the "soup") from droplet based single cell RNA-seq experiments.  Implements the method described in Young et al. (2018) <doi:10.1101/303727>.
	"""
	
	homepage = "https://github.com/constantAmateur/SoupX"
	cran = "SoupX" 

	version("1.6.2", md5="3abad9e262d9e2e6245f1cf1b2058fe0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-seurat@3.2.2:", type=("build", "run"))
