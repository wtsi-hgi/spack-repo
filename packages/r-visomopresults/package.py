# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisomopresults(RPackage):
	"""Graphs and Tables for OMOP Results

	Provides methods to transform omop_result objects into formatted
    tables and figures, facilitating the visualization of study results working 
    with the Observational Medical Outcomes Partnership (OMOP) Common Data 
    Model.
	"""
	
	homepage = "https://oxford-pharmacoepi.github.io/visOmopResults/"
	cran = "visOmopResults" 

	version("0.0.1", md5="ce03e5cccdb36f649590ff41a10b9090")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-omopgenerics@0.0.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
