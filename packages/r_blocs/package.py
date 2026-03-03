# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlocs(RPackage):
	"""Estimate and Visualize Voting Blocs' Partisan Contributions

	Functions to combine data on voting blocs' 
    size, turnout, and vote choice to estimate each bloc's
    vote contributions to the Democratic and Republican parties.
    The package also includes functions for uncertainty estimation and
    plotting. Users may define voting blocs along a discrete or continuous variable.
    The package implements methods described in Grimmer, Marble, and Tanigawa-Lau (2023) <doi:10.31235/osf.io/c9fkg>.
	"""
	
	cran = "blocs" 

	version("0.1.1", md5="19431425f64dd362a2bab03d3df64e90")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-collapse@1.7.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-ks@1.13.4:", type=("build", "run"))
	depends_on("r-mgcv@1.8.39:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
