# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdar(RPackage):
	"""Stratigraphic Data Analysis

	A fast, consistent tool for plotting and facilitating the analysis of stratigraphic
    and sedimentological data. Taking advantage of the flexible plotting tools available in R, 
    'SDAR' uses stratigraphic and sedimentological data to produce detailed graphic logs for 
    outcrop sections and borehole logs. These logs can include multiple features (e.g., bed thickness,
    lithology, samples, sedimentary structures, colors, fossil content, bioturbation index, 
    gamma ray logs) (Johnson, 1992, <ISSN 0037-0738>).
	"""
	
	homepage = "https://doi.org/10.25573/data.13118426.v2"
	cran = "SDAR" 

	version("0.9-55", md5="d25c14db000c590dbb8f23fca8215a2e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-linbin", type=("build", "run"))
	depends_on("r-grimport2", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
