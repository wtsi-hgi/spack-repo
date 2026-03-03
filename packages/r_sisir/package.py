# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSisir(RPackage):
	"""Select Intervals Suited for Functional Regression

	Interval fusion and selection procedures for regression with 
             functional inputs. Methods include a semiparametric approach based
             on Sliced Inverse Regression (SIR), as described in 
             <doi:10.1007/s11222-018-9806-6> (standard ridge and sparse SIR are 
             also included in the package) and a random forest based approach.
	"""
	
	homepage = "https://forgemia.inra.fr/sfcb/sisir"
	cran = "SISIR" 

	version("0.2.2", md5="4513137e8e6809192bed3d31b184ad26")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-boruta", type=("build", "run"))
	depends_on("r-corelearn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-adjclust", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
