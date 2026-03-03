# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWconf(RPackage):
	"""Weighted Confusion Matrix

	Allows users to create weighted confusion matrices and accuracy
    metrics that help with the model selection process for classification
    problems, where distance from the correct category is important. The
    package includes several weighting schemes which can be parameterized, as
    well as custom configuration options. Furthermore, users can decide
    whether they wish to positively or negatively affect the accuracy score
    as a result of applying weights to the confusion matrix. 'wconf' integrates
    well with the 'caret' package, but it can also work standalone when
    provided data in matrix form.
    References:
    Kuhn, M. (2008) "Building Perspective Models in R Using the caret Package"
    <doi:10.18637/jss.v028.i05>
    Monahov, A. (2021) "Model Evaluation with Weighted Threshold Optimization
    (and the mewto R package)" <doi:10.2139/ssrn.3805911>
    Van de Velden, M., Iodice D'Enza, A., Markos, A., Cavicchia, C. (2023)
    "A general framework for implementing distances for categorical variables"
    <arXiv:2301.02190v1>.
	"""
	
	homepage = "https://www.alexandrumonahov.eu.org/projects"
	cran = "wconf" 

	version("1.0.0", md5="ea10941cd8d428e58ea000591c40fc7b")

