# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnap(RPackage):
	"""Simple Neural Application

	A simple wrapper to easily design vanilla deep neural networks using 'Tensorflow'/'Keras' backend for regression, classification and multi-label tasks, with some tweaks and tricks (skip shortcuts, embedding, feature selection and anomaly detection).
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/snap"
	cran = "snap" 

	version("1.1.0", md5="00dd11ffd23a45a3692a842e1f01cc55")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-keras@2.3:", type=("build", "run"))
	depends_on("r-tensorflow@2.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-corelearn@1.54.2:", type=("build", "run"))
	depends_on("r-dbscan@1.1.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-reticulate@1.18:", type=("build", "run"))
