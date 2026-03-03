# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtyd(RPackage):
	"""Implementing BTYD Models with the Log Sum Exp Patch

	Functions for data preparation, parameter estimation, scoring, and plotting for the 
    BG/BB (Fader, Hardie, and Shang 2010 <doi:10.1287/mksc.1100.0580>), 
    BG/NBD (Fader, Hardie, and Lee 2005 <doi:10.1287/mksc.1040.0098>) and 
    Pareto/NBD and Gamma/Gamma (Fader, Hardie, and Lee 2005 <doi:10.1509/jmkr.2005.42.4.415>) models.
	"""
	
	cran = "BTYD" 

	version("2.4.3", md5="c2fdfb366abdc373c73004c35f985bfd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
