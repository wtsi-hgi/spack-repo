# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenskies(RPackage):
	"""Retrieval, Analysis and Visualization of Air Traffic Data

	Provides functionalities and data structures to retrieve, analyze and visualize aviation 
    data. It includes a client interface to the 'OpenSky' API <https://opensky-network.org>. It allows 
    retrieval of flight information, as well as aircraft state vectors.
	"""
	
	cran = "openSkies" 

	version("1.2.1", md5="5b345bd6d846e6c235bf5ce56c0a29c2")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ssh", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rpresto", type=("build", "run"))
