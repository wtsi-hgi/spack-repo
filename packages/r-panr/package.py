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

	version("1.54.0", commit="46ed2cb5d4ab0a0e2cb9839e8134aada8e80b210")
	version("1.48.0", commit="458096dea62bc5bf0a8191cd7ef84c701b6bbefe")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-reder", type=("build", "run"))
