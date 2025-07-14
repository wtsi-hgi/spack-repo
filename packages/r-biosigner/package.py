# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiosigner(RPackage):
	"""Signature discovery from omics data

	Feature selection is critical in omics data analysis to extract restricted and meaningful molecular signatures from complex and high-dimension data, and to build robust classifiers. This package implements a new method to assess the relevance of the variables for the prediction performances of the classifier. The approach can be run in parallel with the PLS-DA, Random Forest, and SVM binary classifiers. The signatures and the corresponding 'restricted' models are returned, enabling future predictions on new datasets. A Galaxy implementation of the package is available within the Workflow4metabolomics.org online infrastructure for computational metabolomics.
	"""
	
	homepage = "http://dx.doi.org/10.3389/fmolb.2016.00026"
	bioc = "biosigner" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biosigner_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biosigner/biosigner_1.30.0.tar.gz"]

	version("1.36.4", tag="RELEASE_3_21")
	version("1.30.0", sha256="c801767a58f46d6c2f96ad550e38f3e9220b232558543e9a69ff1a05379e7cc8")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-multidataset", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ropls", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
