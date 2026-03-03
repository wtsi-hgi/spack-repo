# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlpwr(RPackage):
	"""A Power Analysis Toolbox to Find Cost-Efficient Study Designs

	We implement a surrogate modeling algorithm to guide simulation-based
    sample size planning. The method is described in detail in a recent preprint
    (Zimmer & Debelak (2022) <doi:10.31234/osf.io/tnhb2>).
    It supports multiple study design parameters and optimization with respect to a
    cost function. It can find optimal designs that correspond to a desired 
    statistical power or that fulfill a cost constraint.
	"""
	
	homepage = "https://github.com/flxzimmer/mlpwr"
	cran = "mlpwr" 

	version("1.1.0", md5="8fca4288da83009615cde810d821c7e1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-weightsvm", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
