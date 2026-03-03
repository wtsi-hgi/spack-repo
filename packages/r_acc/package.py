# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcc(RPackage):
	"""Exploring Accelerometer Data

	Processes accelerometer data from uni-axial and tri-axial devices,
    and generates data summaries. Also includes functions to plot, analyze, and
    simulate accelerometer data.
	"""
	
	cran = "acc" 

	version("1.3.3", md5="f5690563afe4e9667f0e090ea93fc633")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mhsmm", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-physicalactivity", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
