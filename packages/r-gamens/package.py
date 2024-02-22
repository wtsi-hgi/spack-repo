# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamens(RPackage):
	"""Applies GAMbag, GAMrsm and GAMens Ensemble Classifiers for
Binary Classification

	Implements the GAMbag, GAMrsm and GAMens ensemble
    classifiers for binary classification (De Bock et al., 2010) <doi:10.1016/j.csda.2009.12.013>. The ensembles
    implement Bagging (Breiman, 1996) <doi:10.1023/A:1010933404324>, the Random Subspace Method (Ho, 1998) <doi:10.1109/34.709601>
    , or both, and use Hastie and Tibshirani's (1990, ISBN:978-0412343902) generalized additive models (GAMs)
    as base classifiers. Once an ensemble classifier has been trained, it can
    be used for predictions on new data. A function for cross validation is also
    included.
	"""
	
	cran = "GAMens" 

	version("1.2.1", md5="88c14cf27b9e064c3407e828406986f9")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
