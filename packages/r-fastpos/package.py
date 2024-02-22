# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastpos(RPackage):
	"""Finds the Critical Sequential Point of Stability for a Pearson
Correlation

	Finds the critical sample size ("critical point of stability") for a 
    correlation to stabilize in Schoenbrodt and Perugini's definition of 
    sequential stability (see <doi:10.1016/j.jrp.2013.05.009>).
	"""
	
	homepage = "https://github.com/johannes-titz/fastpos"
	cran = "fastpos" 

	version("0.5.1", md5="cd72ff4bb7aefd316ff52a1bc77aa924")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
