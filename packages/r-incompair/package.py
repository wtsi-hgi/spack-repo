# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncompair(RPackage):
	"""Comparison of Means for the Incomplete Paired Data

	Implements a variety of nonparametric and parametric methods that are commonly used when the data set is a mixture of paired observations and independent samples. The package also calculates and returns values of different tests with their corresponding p-values.
    Bhoj, D. S. (1991) <doi:10.1002/bimj.4710330108> "Testing equality of means in the presence of correlation and missing data".
    Dubnicka, S. R., Blair, R. C., and Hettmansperger, T. P. (2002) <doi:10.22237/jmasm/1020254460> "Rank-based procedures for mixed paired and two-sample designs".
    Einsporn, R. L. and Habtzghi, D. (2013) <https://pdfs.semanticscholar.org/89a3/90bafeb2bc41ed4414533cfd5ab84a6b54b6.pdf> "Combining paired and two-sample data using a permutation test".
    Ekbohm, G. (1976) <doi:10.1093/biomet/63.2.299> "On comparing means in the paired case with incomplete data on both responses".
    Lin, P. E. and Stivers, L. E. (1974) <doi:10.1093/biomet/61.2.325> On difference of means with incomplete data".
    Maritz, J. S. (1995) <doi:10.1111/j.1467-842x.1995.tb00649.x> "A permutation paired test allowing for missing values".
	"""
	
	cran = "IncomPair" 

	version("0.1.0", md5="ea8041cddc1cd1c0a2fd2efaf5a65ad3")

	depends_on("r@2.10:", type=("build", "run"))
