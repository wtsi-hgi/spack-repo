# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImvol(RPackage):
	"""Volume Prediction of Trees Using Linear and Nonlinear Allometric
Equations

	Volume prediction is one of challenging task in forestry research. This package is a comprehensive toolset designed for the fitting and validation of various linear and nonlinear allometric equations (Linear, Log-Linear, Inverse, Quadratic, Cubic, Compound, Power and Exponential) used in the prediction of conifer tree volume. This package is particularly useful for forestry professionals, researchers, and resource managers engaged in assessing and estimating the volume of coniferous trees. This package has been developed using the algorithm of Sharma et al. (2017) <doi:10.13140/RG.2.2.33786.62407>.
	"""
	
	cran = "ImVol" 

	version("0.1.0", md5="39802ad01bd08b30d4af1fdfd6832208")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
