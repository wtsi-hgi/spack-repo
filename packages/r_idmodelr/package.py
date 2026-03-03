# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdmodelr(RPackage):
	"""Infectious Disease Model Library and Utilities

	Explore a range of infectious disease models in a consistent
    framework. The primary aim of 'idmodelr' is to provide a library of
    infectious disease models for researchers, students, and other interested
    individuals. These models can be used to understand the underlying dynamics
    and as a reference point when developing models for research. 'idmodelr'
    also provides a range of utilities. These include: plotting functionality;
    a simulation wrapper; scenario analysis tooling; an interactive dashboard;
    tools for handling mult-dimensional models; and both model and parameter
    look up tables. Unlike other modelling packages such as 'pomp'
    (<https://kingaa.github.io/pomp/>), 'libbi' (<http://libbi.org>)
    and 'EpiModel' (<http://www.epimodel.org>), 'idmodelr' serves primarily as
    an educational resource. It is most comparable to epirecipes
    (<http://epirecip.es/epicookbook/chapters/simple>) but provides a more
    consistent framework, an R based workflow, and additional utility tooling.
    After users have explored model dynamics with 'idmodelr' they may then
    implement their model using one of these packages in order to utilise the
    model fitting tools they provide.  For newer modellers, this package
    reduces the barrier to entry by containing multiple infectious disease
    models, providing a consistent framework for simulation and visualisation,
    and signposting towards other, more research focussed, resources. 
	"""
	
	homepage = "https://samabbott.co.uk/idmodelr/"
	cran = "idmodelr" 

	version("0.4.0", md5="16642a9a32e023d8a50d02d624825a7a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-future@1.14:", type=("build", "run"))
	depends_on("r-furrr@0.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-desolve@1.23:", type=("build", "run"))
