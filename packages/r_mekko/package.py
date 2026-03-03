# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMekko(RPackage):
	"""Variable Width Bar Charts: Bar Mekko

	Create variable width bar charts i.e.
    "bar mekko" charts to include important quantitative context.
    Closely related to mosaic, spine (or spinogram), matrix,
    submarine, olympic, Mondrian or product plots and tree maps.
	"""
	
	cran = "mekko" 

	version("0.1.0", md5="d2a85ee018be9387a083d8f74a712a1b")

	depends_on("r-ggplot2@2:", type=("build", "run"))
