# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpimodel(RPackage):
	"""Mathematical Modeling of Infectious Disease Dynamics

	Tools for simulating mathematical models of infectious disease dynamics.
    Epidemic model classes include deterministic compartmental models, stochastic
    individual-contact models, and stochastic network models. Network models use the
    robust statistical methods of exponential-family random graph models (ERGMs)
    from the Statnet suite of software packages in R. Standard templates for epidemic
    modeling include SI, SIR, and SIS disease types. EpiModel features an API for
    extending these templates to address novel scientific research aims. Full
    methods for EpiModel are detailed in Jenness et al. (2018, <doi:10.18637/jss.v084.i08>).
	"""
	
	homepage = "http://www.epimodel.org/"
	cran = "EpiModel" 

	version("2.4.0", md5="c788ee2026c16369f6f166a5c2e69074")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-desolve@1.21:", type=("build", "run"))
	depends_on("r-networkdynamic@0.11.3:", type=("build", "run"))
	depends_on("r-tergm@4.2:", type=("build", "run"))
	depends_on("r-statnet-common@4.8:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-ergm-ego@1.1:", type=("build", "run"))
	depends_on("r-egor", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-network@1.18.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-networklite@1.0.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
