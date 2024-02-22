# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatdataml(RPackage):
	"""Read and Write StatDataML Files

	Support for reading and writing files in StatDataML---an XML-based data exchange format.
	"""
	
	cran = "StatDataML" 

	version("1.0-27", md5="941a186c0f985837810e338c29bc6a60")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
