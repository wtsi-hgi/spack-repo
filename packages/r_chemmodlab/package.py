# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemmodlab(RPackage):
	"""A Cheminformatics Modeling Laboratory for Fitting and Assessing
Machine Learning Models

	Contains a set of methods for fitting models and methods for
    validating the resulting models. The statistical methodologies comprise
    a comprehensive collection of approaches whose validity and utility have
    been accepted by experts in the Cheminformatics field. As promising new
    methodologies emerge from the statistical and data-mining communities, they
    will be incorporated into the laboratory. These methods are aimed at discovering
    quantitative structure-activity relationships (QSARs). However, the user can
    directly input their own choices of descriptors and responses, so the capability
    for comparing models is effectively unlimited.
	"""
	
	homepage = "https://github.com/jrash/ChemModLab"
	cran = "chemmodlab" 

	version("2.0.0", md5="6136a3d51a79e9e79a15f05077706f2e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-msqc", type=("build", "run"))
	depends_on("r-class@7.3.14:", type=("build", "run"))
	depends_on("r-e1071@1.6.7:", type=("build", "run"))
	depends_on("r-elasticnet@1.1:", type=("build", "run"))
	depends_on("r-lars@1.2:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-nnet@7.3.12:", type=("build", "run"))
	depends_on("r-proc@1.8:", type=("build", "run"))
	depends_on("r-randomforest@4.6.12:", type=("build", "run"))
	depends_on("r-rpart@4.1.10:", type=("build", "run"))
	depends_on("r-tree@1.0.37:", type=("build", "run"))
	depends_on("r-pls@2.5:", type=("build", "run"))
	depends_on("r-caret@6.0.71:", type=("build", "run"))
