# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzec(RPackage):
	"""Easy Interface to Effective Concentration Calculations

	Because fungicide resistance is an important phenotypic trait for
    fungi and oomycetes, it is necessary to have a standardized method of
    statistically analyzing the Effective Concentration (EC) values. This
    package is designed for those who are not terribly familiar with R to be
    able to analyze and plot an entire set of isolates using the 'drc' package.
	"""
	
	homepage = "https://github.com/grunwaldlab/ezec"
	cran = "ezec" 

	version("1.0.1", md5="b1b91b737ac23aa2fb9f78c87313436c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
