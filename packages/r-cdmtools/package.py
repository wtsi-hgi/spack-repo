# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdmtools(RPackage):
	"""Useful Tools for Cognitive Diagnosis Modeling

	Provides useful tools for cognitive diagnosis modeling (CDM). The package includes functions for empirical Q-matrix estimation and validation, such as the Hull method (Nájera, Sorrel, de la Torre, & Abad, 2021, <doi:10.1111/bmsp.12228>) and the discrete factor loading method (Wang, Song, & Ding, 2018, <doi:10.1007/978-3-319-77249-3_29>). It also contains dimensionality assessment procedures for CDM, including parallel analysis and automated fit comparison as explored in Nájera, Abad, and Sorrel (2021, <doi:10.3389/fpsyg.2021.614470>). Other relevant methods and features for CDM applications, such as the restricted DINA model (Nájera et al., 2023; <doi:10.3102/10769986231158829>), the general nonparametric classification method (Chiu et al., 2018; <doi:10.1007/s11336-017-9595-4>), and corrected estimation of the classification accuracy via multiple imputation (Kreitchmann et al., 2022; <doi:10.3758/s13428-022-01967-5>) are also available. Lastly, the package provides some useful functions for CDM simulation studies, such as random Q-matrix generation and detection of complete/identified Q-matrices.
	"""
	
	homepage = "https://github.com/pablo-najera/cdmTools"
	cran = "cdmTools" 

	version("1.0.5", md5="884a7f8849dd6e7d5025a27789dfbe82")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gdina@2.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-psych@1.9.12:", type=("build", "run"))
	depends_on("r-sirt@3.9.4:", type=("build", "run"))
	depends_on("r-gparotation@2014.11.1:", type=("build", "run"))
	depends_on("r-combinat@0.0.8:", type=("build", "run"))
	depends_on("r-fungible", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
