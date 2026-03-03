# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenearead(RPackage):
	"""Package for Reading Binary Files

	Functions and analytics for GENEA-compatible accelerometer data into R objects. 
             See topic 'GENEAread' for an introduction to the package. 
             See <https://activinsights.com/technology/geneactiv/> for more details on the GENEActiv device.
	"""
	
	cran = "GENEAread" 

	version("2.0.9", md5="d6cf1c115a2743688e7af1f19190757e")
	version("2.0.10", md5="8434993238dcca83276ffa3151aa8037")

	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-mmap", type=("build", "run"))
