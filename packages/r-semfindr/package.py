# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemfindr(RPackage):
	"""Influential Cases in Structural Equation Modeling

	Sensitivity analysis in structural equation modeling using
    influence measures and diagnostic plots. Support leave-one-out casewise
    sensitivity analysis presented by Pek and MacCallum (2011)
    <doi:10.1080/00273171.2011.561068> and approximate casewise influence
    using scores and casewise likelihood.
	"""
	
	homepage = "https://sfcheung.github.io/semfindr/"
	cran = "semfindr" 

	version("0.1.6", md5="041657729659079b30abe1b3573cbe1e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
