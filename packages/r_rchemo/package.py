# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRchemo(RPackage):
	"""Dimension Reduction, Regression and Discrimination for
Chemometrics

	Data exploration and prediction with focus on high dimensional data and chemometrics.
    The package was initially designed about partial least squares regression and discrimination models and variants, in particular locally weighted PLS models (LWPLS). Then, it has been expanded to many other methods for analyzing high dimensional data.
    The name 'rchemo' comes from the fact that the package is orientated to chemometrics, but most of the provided methods are fully generic to other domains.
    Functions such as transform(), predict(), coef() and summary() are available. Tuning the predictive models is facilitated by generic functions gridscore() (validation dataset) and gridcv() (cross-validation). Faster versions are also available for models based on latent variables (LVs) (gridscorelv() and gridcvlv()) and ridge regularization (gridscorelb() and gridcvlb()).
	"""
	
	homepage = "https://github.com/ChemHouse-group/rchemo/"
	cran = "rchemo" 

	version("0.1-1", md5="3db64fbc2a39e5ce35c881c1fd7e5ff4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
