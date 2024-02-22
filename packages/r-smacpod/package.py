# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmacpod(RPackage):
	"""Statistical Methods for the Analysis of Case-Control Point Data

	Statistical methods for analyzing case-control point data.  Methods include the ratio of kernel densities, the difference in K Functions, the spatial scan statistic, and q nearest neighbors of cases.
	"""
	
	cran = "smacpod" 

	version("2.6", md5="862712748281d1034e093e59f369fac3")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-smerc", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
