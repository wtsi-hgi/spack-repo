# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcsurvdata(RPackage):
	"""Meta cohort survival data

	This package stores two merged expressionSet objects that contain the gene expression profile and clinical information of -a- six breast cancer cohorts and -b- four colorectal cancer cohorts. Breast cancer data are employed in the vignette of the hrunbiased package for survival analysis of gene signatures.
	"""
	
	homepage = "https://github.com/adricaba/mcsurvdata"
	bioc = "mcsurvdata"

	version("1.26.0", commit="ee330c92c22a25d459c5a15eede92b138d85b0df")
	version("1.20.0", commit="54ba7d63bd76b0d1d09347bdc76bcde516171e63")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

