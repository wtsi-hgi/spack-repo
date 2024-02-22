# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmallstuff(RPackage):
	"""Dr. Small's Functions

	Functions used in courses taught by Dr. Small at Drew University.
	"""
	
	cran = "smallstuff" 

	version("1.0.3", md5="cdd8447bef672fe586d4d51b935609d9")

	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-matlib@0.9.5:", type=("build", "run"))
	depends_on("r-pryr@0.1.5:", type=("build", "run"))
	depends_on("r-class@7.3.20:", type=("build", "run"))
	depends_on("r-igraph@1.3.1:", type=("build", "run"))
	depends_on("r-rocr@1.0.11:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
