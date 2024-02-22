# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStroke(RPackage):
	"""Clinical Stroke Research

	This is an R-toolbox of custom functions for convenient data management 
    and analysis in clinical health research and teaching.
    The package is mainly collected for personal use, but any use beyond that is encouraged.
    This package has migrated functions from 'agdamsbo/daDoctoR', and new functions has been added.
    Version follows months and year. See NEWS/Changelog for release notes.
    This package includes sampled data from the TALOS trial (Kraglund et al (2018) <doi:10.1161/STROKEAHA.117.020067>).
    The win_prob() function is based on work by Zou et al (2022) <doi:10.1161/STROKEAHA.121.037744>.
    The age_calc() function is based on work by Becker (2020) <doi:10.18637/jss.v093.i02>.
	"""
	
	homepage = "https://agdamsbo.github.io/stRoke/"
	cran = "stRoke" 

	version("23.9.1", md5="f992939951c66e9603a90f5dc3d32ac3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-calendar", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtsummary", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rankinplot", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
