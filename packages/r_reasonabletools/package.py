# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReasonabletools(RPackage):
	"""Clean Water Quality Data for NPDES Reasonable Potential Analyses

	Functions for cleaning and summarising water quality data for use in National Pollutant Discharge Elimination Service (NPDES) permit reasonable potential analyses and water quality-based effluent limitation calculations. Procedures are based on those contained in the "Technical Support Document for Water Quality-based Toxics Control", United States Environmental Protection Agency (1991). 
	"""
	
	homepage = "https://github.com/mattreusswig/reasonabletools"
	cran = "reasonabletools" 

	version("0.1", md5="34600d4560882d3488fa515230f2708c")

	depends_on("r@4:", type=("build", "run"))
