# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkafkajars(RPackage):
	"""External Jars Required for Package 'rkafka'

	The 'rkafkajars' package collects all the external jars required for the 'rkafka' package.
	"""
	
	cran = "rkafkajars" 

	version("1.2", md5="a8d77d7ba799509ba21080ad3d3b75df")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
