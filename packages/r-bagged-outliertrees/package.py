# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaggedOutliertrees(RPackage):
	"""Robust Explainable Outlier Detection Based on OutlierTree

	Bagged OutlierTrees is an explainable unsupervised outlier detection method based on an ensemble implementation of the existing OutlierTree procedure (Cortes, 2020). This implementation takes advantage of bootstrap aggregating (bagging) to improve robustness by reducing the possible masking effect and subsequent high variance (similarly to Isolation Forest), hence the name "Bagged OutlierTrees". To learn more about the base procedure OutlierTree (Cortes, 2020), please refer to <arXiv:2001.00636>.
	"""
	
	homepage = "https://github.com/RafaJPSantos/bagged.outliertrees"
	cran = "bagged.outliertrees" 

	version("1.0.0", md5="59d3a4ee3d4f268d611107e0f7102054")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-outliertree", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
