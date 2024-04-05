# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimnph(RPackage):
	"""Simulate Non-Proportional Hazards

	A toolkit for simulation studies concerning time-to-event endpoints
    with non-proportional hazards. 'SimNPH' encompasses functions for simulating
    time-to-event data in various scenarios, simulating different trial designs
    like fixed-followup, event-driven, and group sequential designs. The package
    provides functions to calculate the true values of common summary statistics
    for the implemented scenarios and offers common analysis methods for
    time-to-event data. Helper functions for running simulations with the
    'SimDesign' package and for aggregating and presenting the results are also
    included. Results of the conducted simulation study are available as
    preprint: "A neutral comparison of statistical methods for time-to-event
    analyses under non-proportional hazards", Klinglmueller et al. (2023)
    <doi:10.48550/ARXIV.2310.05622>.
	"""
	
	homepage = "https://simnph.github.io/SimNPH/"
	cran = "SimNPH" 

	version("0.5.5", md5="913befe64705f681091f91fe5b53f8bb")
	version("0.5.4", md5="376ec3afc4e03365b309542d2a955b48")

	depends_on("r-simdesign", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-minipch@0.3:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-nph", type=("build", "run"))
	depends_on("r-nphrct", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
