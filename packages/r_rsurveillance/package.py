# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsurveillance(RPackage):
	"""Design and Analysis of Disease Surveillance Activities

	A range of functions for the design and
    analysis of disease surveillance activities. These functions were
    originally developed for animal health surveillance activities but can be
    equally applied to aquatic animal, wildlife, plant and human health
    surveillance activities. Utilities are included for sample size calculation
    and analysis of representative surveys for disease freedom, risk-based
    studies for disease freedom and for prevalence estimation.
    This package is based on Cameron A., Conraths F., Frohlich A., Schauer B.,
    Schulz K., Sergeant E., Sonnenburg J., Staubach C. (2015). R package of 
    functions for risk-based surveillance. Deliverable 6.24, WP 6 - Decision 
    making tools for implementing risk-based surveillance, Grant Number 
    no. 310806, RISKSUR (<https://www.fp7-risksur.eu/sites/default/files/documents/Deliverables/RISKSUR_%28310806%29_D6.24.pdf>). 
    Many of the 'RSurveillance' functions are incorporated into the 'epitools'
    website: Sergeant, ESG, 2019. Epitools epidemiological calculators. 
    Ausvet Pty Ltd. Available at: <http://epitools.ausvet.com.au>.
	"""
	
	homepage = "https://github.com/roStats/RSurveillance"
	cran = "RSurveillance" 

	version("0.2.1", md5="de70881fb051eb08bf3dd9bafc378047")

	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
