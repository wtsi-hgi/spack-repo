# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKoulmde(RPackage):
	"""Koul's Minimum Distance Estimation in Regression and Image
Segmentation Problems

	Many methods are developed to deal with two major statistical problems: image segmentation 
    and nonparametric estimation in various regression models. Image segmentation is nowadays 
    gaining a lot of attention from various scientific subfields. Especially, image segmentation 
    has been popular in medical research such as magnetic resonance imaging (MRI) analysis. When 
    a patient suffers from some brain diseases such as dementia and Parkinson's disease, 
    those diseases can be easily diagnosed in brain MRI: the area affected by those diseases is 
    brightly expressed in MRI, which is called a white lesion. For the purpose of medical research,
    locating and segment those white lesions in MRI is a critical issue; it can be done
    manually. However, manual segmentation is very expensive in that it is error-prone and demands a huge
    amount of time. Therefore, supervised machine learning has emerged as an alternative solution. 
    Despite its powerful performance in a classification problem such as hand-written digits, supervised 
    machine learning has not shown the same satisfactory result in MRI analysis. Setting aside all issues
    of the supervised machine learning, it exposed a critical problem when employed for MRI analysis: it 
    requires time-consuming data labeling. Thus, there is a strong demand for an unsupervised approach, 
    and this package - based on Hira L. Koul (1986) <DOI:10.1214/aos/1176350059> - proposes an efficient
    method for simple image segmentation - here, "simple" means that an image is black-and-white - which 
    can easily be applied to MRI analysis. This package includes a function GetSegImage(): when a black-and-white
    image is given as an input, GetSegImage() separates an area of white pixels - which corresponds to 
    a white lesion in MRI - from the given image. For the second problem, consider linear regression model and autoregressive model of
    order q where errors in the linear regression model and innovations in the
    autoregression model are independent and symmetrically distributed. Hira L. Koul
    (1986) <DOI:10.1214/aos/1176350059> proposed a nonparametric minimum distance
    estimation method by minimizing L2-type distance between certain weighted
    residual empirical processes. He also proposed a simpler version of the loss
    function by using symmetry of the integrating measure in the distance. Kim
    (2018) <DOI:10.1080/00949655.2017.1392527> proposed a fast computational method
    which enables practitioners to compute the minimum distance estimator of the vector
    of general multiple regression parameters for several integrating measures. This
    package contains three functions: KoulLrMde(), KoulArMde(), and Koul2StageMde().
    The former two provide minimum distance estimators for linear regression model
    and autoregression model, respectively, where both are based on Koul's method.
    These two functions take much less time for the computation than those based
    on parametric minimum distance estimation methods. Koul2StageMde() provides
    estimators for regression and autoregressive coefficients of linear regression
    model with autoregressive errors through minimum distant method of two stages.
    The new version is written in Rcpp and dramatically reduces computational time. 
	"""
	
	cran = "KoulMde" 

	version("3.2.1", md5="21d38ca95394b42730bdea49c69193bb")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
