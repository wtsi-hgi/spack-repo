# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedometrics(RPackage):
	"""Miscellaneous Pedometric Tools

	An R implementation of methods employed in the field of pedometrics, soil science
    discipline dedicated to studying the spatial, temporal, and spatio-temporal variation of soil
    using statistical and computational methods. The methods found here include the calibration of
    linear regression models using covariate selection strategies, computation of summary validation
    statistics for predictions, generation of summary plots, evaluation of the local quality of a
    geostatistical model of uncertainty, and so on. Other functions simply extend the
    functionalities of or facilitate the usage of functions from other packages that are commonly
    used for the analysis of soil data. Formerly available versions of suggested packages no longer
    available from CRAN can be obtained from the CRAN archive
    <https://cran.r-project.org/src/contrib/Archive/>.
	"""
	
	homepage = "https://github.com/Laboratorio-de-Pedometria/pedometrics-package"
	cran = "pedometrics" 

	version("0.12.1", md5="06649534c4f5f463047f0b3cc1cfe03c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
