# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtps(RPackage):
	"""Multi-Task Prediction using Stacking Algorithms

	Simultaneous multiple outcomes prediction based on revised stacking algorithms, which enables the integration of information from predictions of individual models. An implementation of methodologies proposed in our paper: Li Xing, Mary L Lesperance, Xuekui Zhang. (2019)  Bioinformatics, "Simultaneous prediction of multiple outcomes using revised stacking algorithms" <doi:10.1093/bioinformatics/btz531>.
	"""
	
	homepage = "https://doi.org/10.1093/bioinformatics/btz531"
	cran = "MTPS" 

	version("1.0.2", md5="05f7f78dfce3be9c3fc4c9447f12600a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
