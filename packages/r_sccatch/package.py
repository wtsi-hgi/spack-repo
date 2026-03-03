# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSccatch(RPackage):
	"""Single Cell Cluster-Based Annotation Toolkit for Cellular
Heterogeneity

	An automatic cluster-based annotation pipeline based on evidence-based score by matching the marker genes with known cell markers in tissue-specific cell taxonomy reference database for single-cell RNA-seq data. See Shao X, et al (2020) <doi:10.1016/j.isci.2020.100882> for more details.
	"""
	
	homepage = "https://github.com/ZJUFanLab/scCATCH"
	cran = "scCATCH" 

	version("3.2.2", md5="d45027c260956be2dd3fe21b4264fe29")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
