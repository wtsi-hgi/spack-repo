# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzynumbersExt2(RPackage):
	"""Apply Two Fuzzy Numbers on a Monotone Function

	One can easily draw the membership function of f(x,y) by package 'FuzzyNumbers.Ext.2' in which f(.,.) is supposed monotone and x and y are two fuzzy numbers. This work is possible using function f2apply() which is an extension of function fapply() from Package 'FuzzyNumbers' for two-variable monotone functions. Moreover, this package has the ability of computing the core, support and alpha-cuts of the fuzzy-valued final result.
	"""
	
	cran = "FuzzyNumbers.Ext.2" 

	version("3.2", md5="660b64ecadfe5ee9943fd615b0aaae45", url="https://cran.r-project.org/src/contrib/FuzzyNumbers.Ext.2_3.2.tar.gz")

	depends_on("r-fuzzynumbers", type=("build", "run"))
