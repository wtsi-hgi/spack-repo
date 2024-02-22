# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoftclassval(RPackage):
	"""Soft Classification Performance Measures

	An extension of sensitivity, specificity, positive and negative
    predictive value to continuous predicted and reference memberships in
    [0, 1].
	"""
	
	homepage = "http://softclassval.r-forge.r-project.org/"
	cran = "softclassval" 

	version("1.0-20160527", md5="28af03613830ed6898c9f5707d15e3bb")

	depends_on("r-arrayhelpers@0.76:", type=("build", "run"))
	depends_on("r-svunit", type=("build", "run"))
