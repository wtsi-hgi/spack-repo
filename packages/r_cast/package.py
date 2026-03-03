# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCast(RPackage):
	"""'caret' Applications for Spatial-Temporal Models

	Supporting functionality to run 'caret' with spatial or spatial-temporal data. 'caret' is a frequently used package for model training and prediction using machine learning. CAST includes functions to improve spatial or spatial-temporal modelling tasks using 'caret'. It includes the newly suggested 'Nearest neighbor distance matching' cross-validation to estimate the performance of spatial prediction models and allows for spatial variable selection to selects suitable predictor variables in view to their contribution to the spatial model performance. CAST further includes functionality to estimate the (spatial) area of applicability of prediction models. Methods are described in Meyer et al. (2018) <doi:10.1016/j.envsoft.2017.12.001>; Meyer et al. (2019) <doi:10.1016/j.ecolmodel.2019.108815>; Meyer and Pebesma (2021) <doi:10.1111/2041-210X.13650>; Milà et al. (2022) <doi:10.1111/2041-210X.13851>; Meyer and Pebesma (2022) <doi:10.1038/s41467-022-29838-9>; Linnenbrink et al. (2023) <doi:10.5194/egusphere-2023-1308>.
	"""
	
	homepage = "https://github.com/HannaMeyer/CAST"
	cran = "CAST" 

	version("0.9.0", md5="23a419c9aebc7711131a3c4b897e27cb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
