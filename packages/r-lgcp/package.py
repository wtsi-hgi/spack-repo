# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgcp(RPackage):
	"""Log-Gaussian Cox Process

	Spatial and spatio-temporal modelling of point patterns using the
    log-Gaussian Cox process. Bayesian inference for spatial, spatiotemporal,
    multivariate and aggregated point processes using Markov chain Monte Carlo. See Benjamin M. Taylor, Tilman M. Davies, Barry S. Rowlingson, Peter J. Diggle (2015) <doi:10.18637/jss.v063.i07>.
	"""
	
	cran = "lgcp" 

	version("2.0", md5="faa6adc310a13e588e0e82de14f36d84")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-rpanel@1.1.3:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
