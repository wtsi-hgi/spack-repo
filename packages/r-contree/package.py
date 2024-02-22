# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContree(RPackage):
	"""Contrast Trees and Boosting

	Contrast trees represent a new approach for assessing the
    accuracy of many types of machine learning estimates that are not
    amenable to standard (cross) validation methods; see "Contrast
    trees and distribution boosting", Jerome H. Friedman (2020)
    <doi:10.1073/pnas.1921562117>. In situations where inaccuracies
    are detected, boosted contrast trees can often improve
    performance. Functions are provided to to build such trees in
    addition to a special case, distribution boosting, an assumption
    free method for estimating the full probability distribution of an
    outcome variable given any set of joint input predictor variable
    values.
	"""
	
	homepage = "https://jhfhub.github.io/conTree_tutorial/"
	cran = "conTree" 

	version("0.3-1", md5="070dd7cac5baca1b3efd0556d1d30471")

	depends_on("r@3.5:", type=("build", "run"))
