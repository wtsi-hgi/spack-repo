# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmoo(RPackage):
	"""Multi-Objective Optimization in R

	The 'rmoo' package is a framework for multi- and many-objective
        optimization, which allows researchers and users versatility
        in parameter configuration, as well as tools for analysis, replication
        and visualization of results. The 'rmoo' package was built as a fork of
        the 'GA' package by Luca Scrucca(2017) <DOI:10.32614/RJ-2017-008> and
        implementing the Non-Dominated Sorting Genetic Algorithms proposed
        by K. Deb's.
	"""
	
	homepage = "https://github.com/Evolutionary-Optimization-Laboratory/rmoo/"
	cran = "rmoo" 

	version("0.2.0", md5="986e70c775dbfa332f3b6ddfb473913b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
