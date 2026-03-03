# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStream(RPackage):
	"""Infrastructure for Data Stream Mining

	A framework for data stream modeling and associated data mining tasks such as clustering and classification. The development of this package was supported in part by NSF IIS-0948893, NSF CMMI 1728612, and NIH R21HG005912. Hahsler et al (2017) <doi:10.18637/jss.v076.i14>.
	"""
	
	homepage = "https://github.com/mhahsler/stream"
	cran = "stream" 

	version("2.0-1", md5="14d3ec9f07ea3d22424ec0567b14e866")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-proxy@0.4.7:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-dbscan@1.0.0:", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
