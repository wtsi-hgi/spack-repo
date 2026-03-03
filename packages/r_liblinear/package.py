# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiblinear(RPackage):
	"""Linear Predictive Models Based on the LIBLINEAR C/C++ Library

	A wrapper around the LIBLINEAR C/C++ library for machine
        learning (available at
        <https://www.csie.ntu.edu.tw/~cjlin/liblinear/>). LIBLINEAR is
        a simple library for solving large-scale regularized linear
        classification and regression. It currently supports
        L2-regularized classification (such as logistic regression,
        L2-loss linear SVM and L1-loss linear SVM) as well as
        L1-regularized classification (such as L2-loss linear SVM and
        logistic regression) and L2-regularized support vector
        regression (with L1- or L2-loss). The main features of
        LiblineaR include multi-class classification (one-vs-the rest,
        and Crammer & Singer method), cross validation for model
        selection, probability estimates (logistic regression only) or
        weights for unbalanced data. The estimation of the models is
        particularly fast as compared to other libraries.
	"""
	
	homepage = "<https://dnalytics.com/software/liblinear/>"
	cran = "LiblineaR" 

	version("2.10-23", md5="d273f6ac41fba1e7a32e3938f26c433d")

