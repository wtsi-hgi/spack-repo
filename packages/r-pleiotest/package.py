# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPleiotest(RPackage):
	"""Fast Sequential Pleiotropy Test

	It performs a fast multi-trait genome-wide association analysis based on seemingly unrelated regressions. It tests for pleiotropic effects based on a series of Intersection-Union Wald tests. The package can handle large and unbalanced data and plot results.
	"""
	
	homepage = "https://github.com/FerAguate/pleiotest"
	cran = "pleiotest" 

	version("1.0.0", md5="b85a42522b3441691815629b8e183266")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
