# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistry(RPackage):
	"""Enhanced Command History Tracking for R Sessions and Dynamic
Documents

	Automatically tracks and makes programmatically available code
    evaluation history in R sessions and dynamic documents.
	"""
	
	cran = "histry" 

	version("0.2.4", md5="1ba0263c397b60554c0bb1871fd52020")

	depends_on("r-fastdigest", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-roprov", type=("build", "run"))
	depends_on("r-codedepends", type=("build", "run"))
