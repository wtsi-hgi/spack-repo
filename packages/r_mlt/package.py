# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlt(RPackage):
	"""Most Likely Transformations

	Likelihood-based estimation of conditional transformation
  models via the most likely transformation approach described in
  Hothorn et al. (2018) <DOI:10.1111/sjos.12291> and Hothorn (2020)
  <DOI:10.18637/jss.v092.i01>.  
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "mlt" 

	version("1.5-0", md5="232449d471ab0d0cfcb8d30e6f8ed296")

	depends_on("r-basefun@1.1.2:", type=("build", "run"))
	depends_on("r-variables@1.1.0:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-coneproj", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
