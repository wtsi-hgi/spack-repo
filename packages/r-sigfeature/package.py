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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sigFeature_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sigFeature/sigFeature_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="ff0f705b6895c901657d800a5dd2cc4ac504ecec111982f556e31bdb005efd8a")

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
