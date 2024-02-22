# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRddi(RPackage):
	"""R Interface to DDI Codebook 2.5

	A direct interface to the underlying XML representation of DDI Codebook 2.5 with flexible API creation.
	"""
	
	cran = "rddi" 

	version("0.1.1", md5="5731d82c748daf7527d523c1181be3cb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
