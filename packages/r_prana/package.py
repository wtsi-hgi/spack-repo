# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrana(RPackage):
	"""Pseudo-Value Regression Approach for Network Analysis (PRANA)

	A novel pseudo-value regression approach for the differential co-expression network analysis in expression data, which can incorporate additional clinical variables in the model. This is a direct regression modeling for the differential network analysis, and it is therefore computationally amenable for the most users. The full methodological details can be found in Ahn S et al (2023) <doi:10.1186/s12859-022-05123-w>.
	"""
	
	cran = "PRANA" 

	version("1.0.4", md5="ca5333134b6161d6a9b642a444ea6c0f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dnapath", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
