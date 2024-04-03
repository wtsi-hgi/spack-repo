# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeconetcomp(RPackage):
	"""Compare Microbial Networks of 'trans_network' Class of
'microeco' Package

	Compare microbial co-occurrence networks created from 'trans_network' class of 'microeco' package <https://github.com/ChiLiubio/microeco>.
    This package is the extension of 'trans_network' class of 'microeco' package and especially useful when different networks are constructed and analyzed simultaneously.
	"""
	
	homepage = "https://github.com/ChiLiubio/meconetcomp"
	cran = "meconetcomp" 

	version("0.5.0", md5="72b6743be1cc716ef54ddb2d6e40adee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-microeco@1.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
