# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgswissmaps(RPackage):
	"""Offers Various Swiss Maps as Data Frames and 'ggplot2' Objects

	Offers various swiss maps as data frames and 'ggplot2' objects and gives the
    possibility to add layers of data on the maps. Data are publicly available
    from the swiss federal statistical office.
	"""
	
	homepage = "https://github.com/gibonet/ggswissmaps"
	cran = "ggswissmaps" 

	version("0.1.1", md5="5166991e2b5bbba5b436a8056026f17e")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
