# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpmodel(RPackage):
	"""Spatial Statistical Modeling and Prediction

	Fit, summarize, and predict for a variety of spatial statistical models applied to point-referenced and areal (lattice) data. Parameters are estimated using various methods. Additional modeling features include anisotropy, non-spatial random effects, partition factors, big data approaches, and more. Model-fit statistics are used to summarize, visualize, and compare models. Predictions at unobserved locations are readily obtainable. For additional details, see Dumelle et al. (2023) <doi:10.1371/journal.pone.0282524>.
	"""
	
	homepage = "https://usepa.github.io/spmodel/"
	cran = "spmodel" 

	version("0.5.1", md5="7be27cff08407ae4cc41a73983060fcc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
