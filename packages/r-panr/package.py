# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanr(RPackage):
	"""Posterior association networks and functional modules inferred from rich phenotypes of gene perturbations

	This package provides S4 classes and methods for inferring functional gene networks with edges encoding posterior beliefs of gene association types and nodes encoding perturbation effects.
	"""
	
	bioc = "PANR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PANR_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PANR/PANR_1.48.0.tar.gz"]

	version("1.48.0", md5="accc5472b6656e95d885960d9f1ecee3")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-reder", type=("build", "run"))
