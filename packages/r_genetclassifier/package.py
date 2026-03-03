# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenetclassifier(RPackage):
	"""Classify diseases and build associated gene networks using gene expression profiles

	Comprehensive package to automatically train and validate a multi-class SVM classifier based on gene expression data. Provides transparent selection of gene markers, their coexpression networks, and an interface to query the classifier.
	"""
	
	homepage = "http://www.cicancer.org"
	bioc = "geNetClassifier" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/geNetClassifier_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/geNetClassifier/geNetClassifier_1.42.0.tar.gz"]

	version("1.42.0", md5="7fed3e42e9ec93956b71960e271aa090")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-ebarrays", type=("build", "run"))
	depends_on("r-minet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
