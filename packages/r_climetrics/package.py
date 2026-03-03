# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimetrics(RPackage):
	"""Climate Change Metrics

	A framework that facilitates spatio-temporal analysis of climate dynamics through exploring and measuring different dimensions of climate change in space and time.
	"""
	
	homepage = "https://r-gis.net/"
	cran = "climetrics" 

	version("1.0-12", md5="920a9f62d372e249527242f754775b4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rts", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-yaimpute", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
