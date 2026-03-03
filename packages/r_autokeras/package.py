# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutokeras(RPackage):
	"""R Interface to 'AutoKeras'

	R Interface to 'AutoKeras' <https://autokeras.com/>.
    'AutoKeras' is an open source software library for Automated Machine
    Learning (AutoML). The ultimate goal of AutoML is to provide easily
    accessible deep learning tools to domain experts with limited data science
    or machine learning background. 'AutoKeras' provides functions to
    automatically search for architecture and hyperparameters of deep
    learning models.
	"""
	
	homepage = "https://github.com/r-tensorflow/autokeras"
	cran = "autokeras" 

	version("1.0.12", md5="73ff9fe7138e09427b2340f86dbbfb53")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
