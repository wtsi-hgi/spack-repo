# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDenvax(RPackage):
	"""Simple Dengue Test and Vaccinate Cost Thresholds

	Provides the mathematical model described by "Serostatus Testing & Dengue Vaccine Cost-Benefit Thresholds"
    in <doi:10.1098/rsif.2019.0234>.  Using the functions in the package,
    that analysis can be repeated using sample life histories, either synthesized from local seroprevalence data
    using other functions in this package (as in the manuscript) or from some other source.
    The package provides a vignette which walks through the analysis in the publication, as well as a function
    to generate a project skeleton for such an analysis.
	"""
	
	homepage = "https://gitlab.com/cabp_LSHTM/denvax"
	cran = "denvax" 

	version("0.1.2", md5="8d088f0fadd77f089170e12a138d0cf2")

	depends_on("r@3.5:", type=("build", "run"))
