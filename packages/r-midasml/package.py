# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidasml(RPackage):
	"""Estimation and Prediction Methods for High-Dimensional Mixed
Frequency Time Series Data

	The 'midasml' package implements estimation and prediction methods for high-dimensional mixed-frequency (MIDAS) time-series and panel data regression models. The regularized MIDAS models are estimated using orthogonal (e.g. Legendre) polynomials and sparse-group LASSO (sg-LASSO) estimator. For more information on the 'midasml' approach see Babii, Ghysels, and Striaukas (2021, JBES forthcoming) <doi:10.1080/07350015.2021.1899933>. The package is equipped with the fast implementation of the sg-LASSO estimator by means of proximal block coordinate descent. High-dimensional mixed frequency time-series data can also be easily manipulated with functions provided in the package.
	"""
	
	cran = "midasml" 

	version("0.1.10", md5="71df677cbad234e213ba6bfb8d949aad")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
