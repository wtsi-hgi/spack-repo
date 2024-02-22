# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBwstools(RPackage):
	"""Tools for Case 1 Best-Worst Scaling (MaxDiff) Designs

	Tools to design best-worst scaling designs (i.e., balanced incomplete block designs) and
    to analyze data from these designs, using aggregate and individual methods such as: difference 
    scores, Louviere, Lings, Islam, Gudergan, & Flynn (2013) <doi:10.1016/j.ijresmar.2012.10.002>; 
    analytical estimation, Lipovetsky & Conklin (2014) <doi:10.1016/j.jocm.2014.02.001>; empirical 
    Bayes, Lipovetsky & Conklin (2015) <doi:10.1142/S1793536915500028>; Elo, Hollis (2018) 
    <doi:10.3758/s13428-017-0898-2>; and network-based measures.
	"""
	
	homepage = "https://github.com/markhwhiteii/bwsTools"
	cran = "bwsTools" 

	version("1.2.0", md5="965376feb826060f510122f6ea8a9948")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crossdes", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
