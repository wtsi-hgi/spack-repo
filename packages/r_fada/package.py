# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFada(RPackage):
	"""Variable Selection for Supervised Classification in High
Dimension

	The functions provided in the FADA (Factor Adjusted Discriminant Analysis) package aim at performing supervised classification of high-dimensional and correlated profiles. The procedure combines a decorrelation step based on a  
   factor modeling of the dependence among covariates and a classification method. The available methods are Lasso regularized logistic model
    (see Friedman et al. (2010)), sparse linear discriminant analysis (see
    Clemmensen et al. (2011)), shrinkage linear and diagonal discriminant
    analysis (see M. Ahdesmaki et al. (2010)). More methods of classification can be used on the decorrelated data provided by the package FADA.
	"""
	
	cran = "FADA" 

	version("1.3.5", md5="0d64ab0c6605249b71f582a16d0ba828")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-sparselda", type=("build", "run"))
	depends_on("r-sda", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-crossval", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
