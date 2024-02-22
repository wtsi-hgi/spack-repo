# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStudystrap(RPackage):
	"""Study Strap and Multi-Study Learning Algorithms

	Implements multi-study learning algorithms such as 
		merging, the study-specific ensemble (trained-on-observed-studies ensemble) the study strap, 
		the covariate-matched study strap, covariate-profile similarity weighting, and stacking weights. 
		Embedded within the 'caret' framework, this package allows for a wide range of 
		single-study learners (e.g., neural networks, lasso, random forests). 
		The package offers over 20 default similarity measures and allows for specification of custom 
		similarity measures for covariate-profile similarity weighting and an accept/reject step. 
		This implements methods described in Loewinger, Kishida, Patil, and Parmigiani. (2019)
		<doi:10.1101/856385>.
	"""
	
	cran = "studyStrap" 

	version("1.0.0", md5="3d0446a56cae4b32a0238d5da77bff2f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-tidyverse@1.2.1:", type=("build", "run"))
	depends_on("r-pls@2.7.1:", type=("build", "run"))
	depends_on("r-nnls@1.4:", type=("build", "run"))
	depends_on("r-cca@1.2:", type=("build", "run"))
	depends_on("r-matrixcorrelation@0.9.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.2:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
