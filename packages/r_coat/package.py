# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoat(RPackage):
	"""Conditional Method Agreement Trees (COAT)

	Agreement of continuously scaled measurements made by two techniques, devices or methods is usually
             evaluated by the well-established Bland-Altman analysis or plot. Conditional method agreement trees (COAT),
             proposed by Karapetyan, Zeileis, Henriksen, and Hapfelmeier (2023) <doi:10.48550/arXiv.2306.04456>,
             embed the Bland-Altman analysis in the framework of recursive partitioning to explore heterogeneous method
             agreement in dependence of covariates. COAT can also be used to perform a Bland-Altman test for differences
             in method agreement.
	"""
	
	cran = "coat" 

	version("0.2.0", md5="013989f8006f50a7ee537b31d07e2dec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggparty", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
