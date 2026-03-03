# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBonn(RPackage):
	"""Access INKAR Database

	Retrieve and import data from the INKAR database (Indikatoren und Karten zur Raum- und Stadtentwicklung Datenbank, <https://www.inkar.de>) of the Federal Office for Building and Regional Planning (BBSR) in Bonn using their JSON API. 
	"""
	
	homepage = "https://github.com/sumtxt/bonn/"
	cran = "bonn" 

	version("1.0.2", md5="9eb7e3d1fe443c1ff4b23e1176d6612d")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
