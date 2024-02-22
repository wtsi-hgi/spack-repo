# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlocker(RPackage):
	"""Flexible Occupancy Estimation with Stan

	Fit occupancy models in 'Stan' via 'brms'. The full variety
    of 'brms' formula-based effects structures are available to use in
    multiple classes of occupancy model, including single-season
    models, models with data augmentation for never-observed species,
    dynamic (multiseason) models with explicit colonization and extinction
    processes, and dynamic models with autologistic occupancy dynamics.
    Formulas can be specified for all relevant distributional terms,
    including detection and one or more of occupancy, colonization,
    extinction, and autologistic depending on the model type. Several
    important forms of model post-processing are provided.  References:
    Bürkner (2017) <doi:10.18637/jss.v080.i01>; Carpenter et al. (2017)
    <doi:10.18637/jss.v076.i01>; Socolar & Mills (2023)
    <doi:10.1101/2023.10.26.564080>.
	"""
	
	homepage = "https://github.com/jsocolar/flocker"
	cran = "flocker" 

	version("1.0-0", md5="a4dc6715a1e138d1e6080b0abbce9800")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-brms@2.20.3:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
