# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMltDocreg(RPackage):
	"""Most Likely Transformations: Documentation and Regression Tests

	Additional documentation, a package vignette and 
  regression tests for package mlt.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "mlt.docreg" 

	version("1.1-7", md5="d2400f6c99c9f8c89f63411cc81780a2")

	depends_on("r-mlt@1.3.2:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-eha", type=("build", "run"))
	depends_on("r-multcomp@1.4.4:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-truncreg", type=("build", "run"))
