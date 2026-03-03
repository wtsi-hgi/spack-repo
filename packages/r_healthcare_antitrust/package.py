# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthcareAntitrust(RPackage):
	"""Healthcare Antitrust Analysis

	Antitrust analysis of
    healthcare markets. Contains functions to implement the 
    semiparametric estimation technique described in Raval, Rosenbaum,
    and Tenn (2017) "A Semiparametric Discrete Choice Model: An Application
    to Hospital Mergers" <doi:10.1111/ecin.12454>.
	"""
	
	homepage = "https://github.com/mpanhans/healthcare.antitrust"
	cran = "healthcare.antitrust" 

	version("0.1.4", md5="22380b67b5e60b9f04fe2d3461371a7e")

	depends_on("r@2.10:", type=("build", "run"))
