# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecrdesign(RPackage):
	"""Sampling Design for Spatially Explicit Capture-Recapture

	Tools for designing spatially explicit capture-recapture studies of animal populations. This is primarily a simulation manager for package 'secr'. Extensions in version 2.5.0 include costing and evaluation of detector spacing.
	"""
	
	homepage = "https://www.otago.ac.nz/density/"
	cran = "secrdesign" 

	version("2.8.2", md5="4a6de77f8d6f439af80dbae38499050e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-secr@4.2:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-kofnga", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
