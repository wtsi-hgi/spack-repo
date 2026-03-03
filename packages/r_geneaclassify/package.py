# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneaclassify(RPackage):
	"""Segmentation and Classification of Accelerometer Data

	Segmentation and classification procedures for data from the 'Activinsights GENEActiv' <https://activinsights.com/technology/geneactiv/> accelerometer that provides the user with a model to guess behaviour from test data where behaviour is missing.
    Includes a step counting algorithm, a function to create segmented data with custom features and a function to use recursive partitioning provided in the function rpart() of the 'rpart' package to create classification models.
	"""
	
	cran = "GENEAclassify" 

	version("1.5.5", md5="b502597f5423195ac867869fa1d65fae")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genearead", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
