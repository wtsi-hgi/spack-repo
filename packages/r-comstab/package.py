# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComstab(RPackage):
	"""Partitioning the Drivers of Stability of Ecological Communities

	Contains the basic functions to apply the unified framework
    for partitioning the drivers of stability of ecological communities. 
    J. Segrestin, L. Götzenberger, E. Valencia, F. de Bello & J. Lepš (2024) 
    "A unified framework for partitioning the drivers of stability of ecological communities" <minor revisions>.
	"""
	
	homepage = "https://github.com/jsegrestin/comstab"
	cran = "comstab" 

	version("0.0.1", md5="769558036262b09b784d1bdf89632e45")

	depends_on("r-ternary", type=("build", "run"))
