# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMflica(RPackage):
	"""Leadership-Inference Framework for Multivariate Time Series

	A leadership-inference framework for multivariate time series. The framework for multiple-faction-leadership inference from coordinated activities or 'mFLICA' uses a notion of a leader as an individual who initiates collective patterns that everyone in a group follows. Given a set of time series of individual activities, our goal is to identify periods of coordinated activity, find factions of coordination if more than one exist, as well as identify leaders of each faction. For each time step, the framework infers following relations between individual time series, then identifying a leader of each faction whom many individuals follow but it follows no one. A faction is defined as a group of individuals that everyone follows the same leader. 'mFLICA' reports following relations, leaders of factions, and members of each faction for each time step. Please see Chainarong Amornbunchornvej and Tanya Berger-Wolf (2018) <doi:10.1137/1.9781611975321.62> for methodology and Chainarong Amornbunchornvej (2021) <doi:10.1016/j.softx.2021.100781> for software when referring to this package in publications.
	"""
	
	homepage = "https://github.com/DarkEyes/mFLICA"
	cran = "mFLICA" 

	version("0.1.5", md5="d7e86d3154cdeb854128ebb0d1a0bc3d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
