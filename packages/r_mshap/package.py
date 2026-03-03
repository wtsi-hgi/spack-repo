# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMshap(RPackage):
	"""Multiplicative SHAP Values for Two-Part Models

	Allows for the computation of mSHAP values on
    two-part models as proposed  by Matthews, S. and Hartman, B. 
    (2021) <arXiv:2106.08990>.
    Also contains functions for simple plotting of
    the results (or any SHAP values). For information about the
    TreeSHAP algorithm that mSHAP builds on, see Lundberg, S.M.,
    Erion, G., Chen, H., DeGrave, A., Prutkin, J.M., Nair, B., Katz,
    R., Himmelfarb, J., Bansal, N., Lee, S.I. (2020)
    <doi:10.1038/s42256-019-0138-9>.
	"""
	
	cran = "mshap" 

	version("0.1.0", md5="e4a895a3e1da4670f8b9b5f7fd991ed6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.4:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
