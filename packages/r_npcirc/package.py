# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcirc(RPackage):
	"""Nonparametric Circular Methods

	Nonparametric smoothing methods for density and regression estimation involving circular data, 
				including the estimation of the mean regression function and other conditional characteristics.
	"""
	
	homepage = "https://www.jstatsoft.org/v61/i09/"
	cran = "NPCirc" 

	version("3.1.1", md5="990dc89c86e32419e69a0c14374c10af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-bolstad2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
