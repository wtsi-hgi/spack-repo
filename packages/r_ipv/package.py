# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpv(RPackage):
	"""Item Pool Visualization

	Generate plots based on the Item Pool Visualization concept for
    latent constructs. Item Pool Visualizations are used to display the
    conceptual structure of a set of items (self-report or psychometric).
    Dantlgraber, Stieger, & Reips (2019) <doi:10.1177/2059799119884283>.
	"""
	
	homepage = "https://github.com/NilsPetras/IPV"
	cran = "IPV" 

	version("1.0.0", md5="b09a0b65452fc588c5f9a33ba977429a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
