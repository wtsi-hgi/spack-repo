# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNproc(RPackage):
	"""Neyman-Pearson (NP) Classification Algorithms and NP Receiver
Operating Characteristic (NP-ROC) Curves

	In many binary classification applications, such as disease
    diagnosis and spam detection, practitioners commonly face the need to limit
    type I error (i.e., the conditional probability of misclassifying a class 0
    observation as class 1) so that it remains below a desired threshold. To address
    this need, the Neyman-Pearson (NP) classification paradigm is a natural choice;
    it minimizes type II error (i.e., the conditional probability of misclassifying
    a class 1 observation as class 0) while enforcing an upper bound, alpha, on the
    type I error. Although the NP paradigm has a century-long history in hypothesis
    testing, it has not been well recognized and implemented in classification
    schemes. Common practices that directly limit the empirical type I error to
    no more than alpha do not satisfy the type I error control objective because
    the resulting classifiers are still likely to have type I errors much larger
    than alpha. As a result, the NP paradigm has not been properly implemented
    for many classification scenarios in practice. In this work, we develop the
    first umbrella algorithm that implements the NP paradigm for all scoring-type
    classification methods, including popular methods such as logistic regression,
    support vector machines and random forests. Powered by this umbrella algorithm,
    we propose a novel graphical tool for NP classification methods: NP receiver
    operating characteristic (NP-ROC) bands, motivated by the popular receiver
    operating characteristic (ROC) curves. NP-ROC bands will help choose in a data
    adaptive way and compare different NP classifiers. 
	"""
	
	homepage = "http://advances.sciencemag.org/content/4/2/eaao1659"
	cran = "nproc" 

	version("2.1.5", md5="c1bfc6a8121d5a4d734cf6f4e9445695")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-naivebayes", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ada", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-tree", type=("build", "run"))
