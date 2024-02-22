# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeostatsp(RPackage):
	"""Geostatistical Modelling with Likelihood and Bayes

	Geostatistical modelling facilities using 'SpatRaster' and 'SpatVector'
    objects are provided. Non-Gaussian models are fit using 'INLA', and Gaussian
    geostatistical models use Maximum Likelihood Estimation.  For details see Brown (2015) <doi:10.18637/jss.v063.i12>. The 'RandomFields' package is available at <https://www.wim.uni-mannheim.de/schlather/publications/software>.
	"""
	
	cran = "geostatsp" 

	version("2.0.6", md5="e7f03b1e64bade28a8841cc9178b4e7e")

	depends_on("r-matrix@1.6.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
