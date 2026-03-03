# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoex(RPackage):
	"""The One-Way Heteroscedastic ANOVA Tests

	Contains the heteroscedastic ANOVA tests for normal and two-parameter exponential distributed populations. For normal distributions, Alexander-Govern test by Alexandern and Govern (1994) <doi:10.2307/1165140>, Alvandi et al. Generalized F test by Alvandi et al. (2012) <doi:10.1080/03610926.2011.573160>, Approximate F test by Asiribo and Gurland (1990) <doi:10.1080/03610929008830427>, Box F test by Box (1954) <doi:10.1214/aoms/1177728786>, Brown-Forsythe test by Brown and Forsythe (1974) <do:10.2307/1267501>, B2 test by Ozdemir and Kurt (2006) <http://sjam.selcuk.edu.tr/sjam/article/view/174>, Cochran F test by Cochran (1937) <https://www.jstor.org/stable/pdf/2984123.pdf>, Fiducial Approach test by Li et al. (2011) <doi:10.1016/j.csda.2010.12.009>, Generalized F test by Weerahandi (1995) <doi:10.2307/2532947>, Johansen F test by Johansen (1980) <doi:10.1093/biomet/67.1.85>, Modified Brown-Forsythe test by Mehrotra (1997) <doi:10.1080/03610919708813431>, Modified Welch test by Hartung et al.(2002) <doi:10.1007/s00362-002-0097-8>, One-Stage test by Chen and Chen (1998) <doi:10.1080/03610919808813501>, One-Stage Range test by Chen and Chen (2000) <doi:10.1080/01966324.2000.10737505>, Parametric Bootstrap test by Krishnamoorhty et al.(2007) <doi:10.1016/j.csda.2006.09.039>, Permutation F test by Berry and Mielke (2002) <doi:10.2466/pr0.2002.90.2.495>, Scott-Smith test by Scott and Smith (1971) <doi:10.2307/2346757>, Welch test by Welch(1951) <doi:10.2307/2332579>, and Welch-Aspin test by Aspin (1948) <doi:10.1093/biomet/35.1-2.88>. These tests are used to test the equality of group means under unequal variance. Also, a modified version of Generalized F-test is improved to test the equality of non-normal group means under unequal variances and a revised version of Generalized F-test is given to test the equality of non-normal group means caused by skewness. Furthermore, it consists some procedures for testing equality of several two-parameter exponentially distributed population means under unequal scale parameters such as generalized p-value, parametric bootstrap and fiducial approach test by Malekzadeh and Jafari (2019) <doi:10.1080/03610918.2018.1538452>. There is also Hsieh test by Hsieh (1986) <doi:10.2307/1270452> for testing equality of location parameters of two-parameter exponentially distributed populations under unequal scale parameters.
	"""
	
	cran = "doex" 

	version("1.2", md5="40e932ec743ae1bc7934db6b6aa3cdf6")

