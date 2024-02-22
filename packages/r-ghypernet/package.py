# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhypernet(RPackage):
	"""Fit and Simulate Generalised Hypergeometric Ensembles of Graphs

	Provides functions for model fitting and selection of generalised hypergeometric ensembles of random graphs (gHypEG).
    To learn how to use it, check the vignettes for a quick tutorial.
    Please reference its use as Casiraghi, G., Nanumyan, V. (2019) <doi:10.5281/zenodo.2555300>
    together with those relevant references from the one listed below.
    The package is based on the research developed at the Chair of Systems Design, ETH Zurich.
    Casiraghi, G., Nanumyan, V., Scholtes, I., Schweitzer, F. (2016) <arXiv:1607.02441>.
    Casiraghi, G., Nanumyan, V., Scholtes, I., Schweitzer, F. (2017) <doi:10.1007/978-3-319-67256-4_11>.
    Casiraghi, G., (2017) <arXiv:1702.02048>
    Brandenberger, L., Casiraghi, G., Nanumyan, V., Schweitzer, F. (2019) <doi:10.1145/3341161.3342926>
    Casiraghi, G. (2019) <doi:10.1007/s41109-019-0241-1>.
    Casiraghi, G., Nanumyan, V. (2021) <doi:10.1038/s41598-021-92519-y>.
    Casiraghi, G. (2021) <doi:10.1088/2632-072X/ac0493>.
	"""
	
	homepage = "https://ghyper.net"
	cran = "ghypernet" 

	version("1.1.0", md5="96ba884f3470ffc576f71dcda4435240")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-texreg", type=("build", "run"))
