# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiplab(RPackage):
	"""Spatial Individual-Plant Modelling

	A platform for computing competition indices and experimenting
    with spatially explicit individual-based vegetation models.
	"""
	
	homepage = "https://github.com/ogarciav/siplab/"
	cran = "siplab" 

	version("1.6", md5="03e40f3e085c7b722ad28c1753809596")

	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
