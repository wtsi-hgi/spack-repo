# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntegratedjm(RPackage):
	"""Joint Modeling of the Gene-Expression and Bioassay Data, Taking
Care of the Effect Due to a Fingerprint Feature

	Offers modeling the association between gene-expression and bioassay data, taking care of the effect due to a fingerprint feature and helps with several plots to better understand the analysis.
	"""
	
	cran = "IntegratedJM" 

	version("1.6", md5="889773b4b8bbec28c4f4792741ed04c9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
