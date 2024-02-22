# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArt(RPackage):
	"""Aligned Rank Transform for Nonparametric Factorial Analysis

	An implementation of the Aligned Rank Transform technique for
    factorial analysis (see references below for details) including models with
    missing terms (unsaturated factorial models). The function first
    computes a separate aligned ranked response variable for each effect of the
    user-specified model, and then runs a classic ANOVA on each of the aligned
    ranked responses. For further details, see Higgins, J. J. and Tashtoush, S.
    (1994). An aligned rank transform test for interaction. Nonlinear World 1
    (2), pp. 201-211. Wobbrock, J.O., Findlater, L., Gergle, D. and
    Higgins,J.J. (2011). The Aligned Rank Transform for nonparametric factorial
    analyses using only ANOVA procedures. Proceedings of the ACM Conference on
    Human Factors in Computing Systems (CHI '11). New York: ACM Press, pp.
    143-146. <doi:10.1145/1978942.1978963>.
	"""
	
	homepage = "http://decsai.ugr.es/~pjvi/r-packages.html"
	cran = "ART" 

	version("1.0", md5="2bec1888f0de3add8572892ca20952d6")

	depends_on("r-car", type=("build", "run"))
