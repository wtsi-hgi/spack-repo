# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubscreen(RPackage):
	"""Systematic Screening of Study Data for Subgroup Effects

	Identifying outcome relevant subgroups has now become as simple as possible! The formerly lengthy and tedious search for the needle in a haystack will be replaced by a single, comprehensive and coherent presentation.
 The central result of a subgroup screening is a diagram in which each single dot stands for a subgroup.
 The diagram may show thousands of them. The position of the dot in the diagram is determined by the
 sample size of the subgroup and the statistical measure of the treatment effect in that subgroup. The
 sample size is shown on the horizontal axis while the treatment effect is displayed on the vertical axis. Furthermore,
 the diagram shows the line of no effect and the overall study results. For small subgroups, which
 are found on the left side of the plot, larger random deviations from the mean study effect are expected,
 while for larger subgroups only small deviations from the study mean can be expected to be chance findings.
 So for a study with no conspicuous subgroup effects, the dots in the figure are expected to form a
 kind of funnel. Any deviations from this funnel shape hint to conspicuous subgroups.
 This approach was presented in Muysers (2020) <doi:10.1007/s43441-019-00082-6> and referenced in Ballarini (2020) <doi:10.1002/pst.2012>.
 New to version 3 is the Automatic Screening of one- or MUlti-factorial Subgroups (ASMUS) for documentation of the structured review of subgroup findings.
	"""
	
	cran = "subscreen" 

	version("3.0.7", md5="781d527fe8a22d7b02dda15009768a28")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
