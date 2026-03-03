# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvpot(RPackage):
	"""Multivariate Peaks-over-Threshold Modelling for Spatial Extreme
Events

	Tools for high-dimensional peaks-over-threshold inference and simulation
  of spatial extremal processes. Key references include de Fondeville and Davison (2018) <doi:10.1093/biomet/asy026>, Thibaud and Opitz (2015) <doi:10.1093/biomet/asv045>, Wadsworth and Tawn <doi:10.1093/biomet/ast042>.
	"""
	
	homepage = "https://github.com/r-fndv/mvPot"
	cran = "mvPot" 

	version("0.1.6", md5="29feeb2f009295287b790ddf4e411704")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
