# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMolar(RPackage):
	"""Dental Surface Complexity Measurement Tools

	Surface topography calculations of Dirichlet's normal energy,
    relief index, surface slope, and orientation patch count for teeth using scans of
    enamel caps.
    Importantly, for the relief index and orientation patch count calculations to
    work, the scanned tooth files must be oriented with the occlusal plane parallel
    to the x and y axes, and perpendicular to the z axis. The files should also be
    simplified, and smoothed in some other software prior to uploading into R.
	"""
	
	cran = "molaR" 

	version("5.3", md5="f30fd43b387cb59c97ec819618eb8cd5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-alphahull", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
