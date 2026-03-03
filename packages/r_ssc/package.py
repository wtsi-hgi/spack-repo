# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsc(RPackage):
	"""Semi-Supervised Classification Methods

	Provides a collection of self-labeled techniques for semi-supervised 
    classification. In semi-supervised classification, both labeled and unlabeled
    data are used to train a classifier. This learning paradigm has obtained promising
    results, specifically in the presence of a reduced set of labeled examples. 
    This package implements a collection of self-labeled techniques to construct a
    classification model. This family of techniques enlarges the original labeled set 
	using the most confident predictions to classify unlabeled data. The techniques 
	implemented can be applied to classification problems in several domains by the 
	specification of a supervised base classifier. At low ratios of labeled data, it 
	can be shown to perform better than classical supervised classifiers.
	"""
	
	homepage = "https://github.com/mabelc/SSC"
	cran = "ssc" 

	version("2.1-0", md5="122e647cfaf26507b92a546dab33e053")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
