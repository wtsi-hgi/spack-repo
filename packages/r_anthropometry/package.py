# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnthropometry(RPackage):
	"""Statistical Methods for Anthropometric Data

	Statistical methodologies especially developed to analyze anthropometric data. These methods are aimed 		at providing effective solutions to some commons problems related to Ergonomics and Anthropometry. They are based on clustering, the 		statistical concept of data depth, statistical shape analysis and archetypal analysis. Please see Vinue (2017) <doi:10.18637/jss.v077.i06>.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "Anthropometry" 

	version("1.19", md5="0601e2b87c3afdd6c9d92e0f1ab5fb27")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-shapes", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-archetypes", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-ddalpha", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-icge", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-biclust", type=("build", "run"))
