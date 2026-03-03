# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeasonalclumped(RPackage):
	"""Toolbox for Clumped Isotope Seasonality Reconstructions

	Compiles a set of functions and dummy data that simplify reconstructions of seasonal temperature
	 variability in the geological past from stable isotope and clumped isotope records in sub–annually resolved
	 carbonate archives (e.g. mollusk shells, corals and speleothems). For more information, see
	 de Winter et al., 2020 (Climate of the Past Discussions, <doi:10.5194/cp-2020-118>).
	"""
	
	homepage = "https://github.com/nielsjdewinter/seasonalclumped"
	cran = "seasonalclumped" 

	version("0.3.2", md5="f8a8036725f899198479740bda238e7a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
