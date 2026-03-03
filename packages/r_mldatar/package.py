# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMldatar(RPackage):
	"""Collection of Machine Learning Datasets for Supervised Machine
Learning

	Contains a collection of datasets for working with machine learning tasks.
    It will contain datasets for supervised machine learning Jiang (2020)<doi:10.1016/j.beth.2020.05.002> and will include datasets for classification and regression.
    The aim of this package is to use data generated around health and other domains.
	"""
	
	cran = "MLDataR" 

	version("1.0.1", md5="b30fd354073d576f62b543be591fef97")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-confusiontabler", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-varhandle", type=("build", "run"))
	depends_on("r-oddsplotty", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
