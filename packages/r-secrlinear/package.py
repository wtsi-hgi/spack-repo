# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecrlinear(RPackage):
	"""Spatially Explicit Capture-Recapture for Linear Habitats

	Tools for spatially explicit capture-recapture analysis of animal populations in linear habitats, extending package 'secr'.
	"""
	
	homepage = "https://www.otago.ac.nz/density/"
	cran = "secrlinear" 

	version("1.2.2", md5="cbc3a8288235ac0d10f6dadf4aa48224")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-secr@3.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
