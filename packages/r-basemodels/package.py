# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasemodels(RPackage):
	"""Baseline Models for Classification and Regression

	Providing equivalent functions for the dummy
    classifier and regressor used in 'Python' 'scikit-learn' library. Our goal
    is to allow R users to easily identify baseline performance for their
    classification and regression problems. Our baseline models use no
    predictors, and are useful in cases of class imbalance, multiclass
    classification, and when users want to quickly identify how much
    improvement their statistical and machine learning models are over several
    baseline models. We use a "better" default (proportional guessing) for
    the dummy classifier than the 'Python' implementation ("prior", which is
    the most frequent class in the training set). The functions in the
    package can be used on their own, or introduce methods named
    'dummy_regressor' or 'dummy_classifier' that can be used within the
    caret package pipeline.
	"""
	
	homepage = "https://github.com/Ying-Ju/basemodels"
	cran = "basemodels" 

	version("1.1.0", md5="83cf4cb237c10ec920cd58bf74ee55ab")

