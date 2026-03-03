# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtocen(RPackage):
	"""Quantile-Optimal Treatment Regimes with Censored Data

	Provides methods for estimation of mean- and quantile-optimal treatment regimes from censored data. 
    Specifically, we have developed distinct functions for three types of right censoring for static treatment using quantile criterion: (1) independent/random censoring, (2) treatment-dependent random censoring, and (3) covariates-dependent random censoring. It also includes a function to estimate quantile-optimal dynamic treatment regimes for independent censored data. Finally, this package also includes a simulation data generative model of a dynamic treatment experiment proposed in literature.
	"""
	
	cran = "QTOCen" 

	version("0.1.1", md5="b13ef72bfad93b6510ce46d50799413a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rgenoud@5.8:", type=("build", "run"))
	depends_on("r-quantreg@5.18:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
