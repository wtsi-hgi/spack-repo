# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedfate(RPackage):
	"""Mediterranean Forest Simulation

	Simulate Mediterranean forest functioning and dynamics using cohort-based description of vegetation [De Caceres et al. (2015) <doi:10.1016/j.agrformet.2015.06.012>; De Caceres et al. (2021) <doi:10.1016/j.agrformet.2020.108233>].
	"""
	
	homepage = "https://emf-creaf.github.io/medfate/"
	cran = "medfate" 

	version("3.2.0", md5="262754edd02d5409df66e1e6918e0559")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-meteoland", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
