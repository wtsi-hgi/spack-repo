# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuperdec(RPackage):
	"""Cumulative Percent Decay Curve Generator

	Calculates and visualises cumulative percent 'decay' curves,
    which are typically calculated from metagenomic taxonomic profiles.
    These can be used to estimate the level of expected 'endogenous' taxa
    at different abundance levels retrieved from metagenomic samples, when
    comparing to samples of known sampling site or source. Method
    described in Fellows Yates, J. A. et. al. (2021) Proceedings of the
    National Academy of Sciences USA <doi:10.1073/pnas.2021655118>.
	"""
	
	homepage = "https://github.com/jfy133/cuperdec"
	cran = "cuperdec" 

	version("1.1.0", md5="fdfcce1a5042c502ddab7811e32243ca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
