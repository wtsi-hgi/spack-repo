# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcc(RPackage):
	"""Simulation and Analysis of Platform Trials with Non-Concurrent
Controls

	Design and analysis of flexible platform trials with non-concurrent controls. Functions for data generation, analysis, visualization and running simulation studies are provided. 
    The implemented analysis methods are described in: 
    Bofill Roig et al. (2022) <doi:10.1186/s12874-022-01683-w>, 
    Saville et al. (2022) <doi:10.1177/17407745221112013> and 
    Schmidli et al. (2014) <doi:10.1111/biom.12242>.
	"""
	
	homepage = "https://pavlakrotka.github.io/NCC/"
	cran = "NCC" 

	version("1.0", md5="c78b88ccfd0f80631a7e57acf00ae1a3")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rbest", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-spamm", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
