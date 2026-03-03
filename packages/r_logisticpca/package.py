# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogisticpca(RPackage):
	"""Binary Dimensionality Reduction

	Dimensionality reduction techniques for binary data including
    logistic PCA.
	"""
	
	homepage = "https://github.com/andland/logisticPCA"
	cran = "logisticPCA" 

	version("0.2", md5="ba72f58587cac8f9c6fbb591dbe8623d")

	depends_on("r-ggplot2", type=("build", "run"))
