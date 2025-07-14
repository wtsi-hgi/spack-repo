# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigfeature(RPackage):
	"""sigFeature: Significant feature selection using SVM-RFE & t-statistic

	This package provides a novel feature selection algorithm for binary classification using support vector machine recursive feature elimination SVM-RFE and t-statistic. In this feature selection process, the selected features are differentially significant between the two classes and also they are good classifier with higher degree of classification accuracy.
	"""
	
	bioc = "sigFeature"

	version("1.26.0", commit="a618cd7570cd5c3ddb208902b3f497b4934deb6e")
	version("1.20.0", commit="251052270223cf1455c6becc256c380ca70b73e6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocviews", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
