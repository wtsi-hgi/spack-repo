# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFealect(RPackage):
	"""Scores Features for Feature Selection

	For each feature, a score is computed that can be useful
        for feature selection. Several random subsets are sampled from
        the input data and for each random subset, various linear
        models are fitted using lars method. A score is assigned to
        each feature based on the tendency of LASSO in including that
        feature in the models.Finally, the average score and the models
        are returned as the output. The features with relatively low
        scores are recommended to be ignored because they can lead to
        overfitting of the model to the training data. Moreover, for
        each random subset, the best set of features in terms of global
        error is returned. They are useful for applying Bolasso, the
        alternative feature selection method that recommends the
        intersection of features subsets.
	"""
	
	cran = "FeaLect" 

	version("1.20", md5="4200207294b4d89ddc2f8d336b279e41")

	depends_on("r-lars", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
