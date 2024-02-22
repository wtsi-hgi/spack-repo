# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexmex(RPackage):
	"""Statistical Modelling of Extreme Values

	Statistical extreme value modelling of threshold excesses, maxima
    and multivariate extremes. Univariate models for threshold excesses and maxima
    are the Generalised Pareto, and Generalised Extreme Value model respectively.
    These models may be fitted by using maximum (optionally penalised-)likelihood,
    or Bayesian estimation, and both classes of models may be fitted with covariates
    in any/all model parameters. Model diagnostics support the fitting process.
    Graphical output for visualising fitted models and return level estimates is
    provided. For serially dependent sequences, the intervals declustering algorithm
    of Ferro and Segers (2003) <doi:10.1111/1467-9868.00401> is provided, with
    diagnostic support to aid selection of threshold and declustering horizon.
    Multivariate modelling is performed via the conditional approach of Heffernan
    and Tawn (2004) <doi:10.1111/j.1467-9868.2004.02050.x>, with graphical tools for
    threshold selection and to diagnose estimation convergence.
	"""
	
	homepage = "https://github.com/harrysouthworth/texmex"
	cran = "texmex" 

	version("2.4.8", md5="fd45bdc6c105073249c59999c70c4f58")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
