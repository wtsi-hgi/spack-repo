# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnetwosamples(RPackage):
	"""Deal with One and Two (Normal) Samples

	We introduce an R function
        one_two_sample() which can deal with one and two (normal)
        samples, Ying-Ying Zhang, Yi Wei (2012) <doi:10.2991/asshm-13.2013.29>. 
        For one normal sample x, the function reports
        descriptive statistics, plot, interval estimation and test of
        hypothesis of x. For two normal samples x and y, the function
        reports descriptive statistics, plot, interval estimation and
        test of hypothesis of x and y, respectively. It also reports
        interval estimation and test of hypothesis of mu1-mu2 (the
        difference of the means of x and y) and sigma1^2 / sigma2^2
        (the ratio of the variances of x and y), tests whether x and y
        are from the same population, finds the correlation coefficient
        of x and y if x and y have the same length.
	"""
	
	cran = "OneTwoSamples" 

	version("1.1-0", md5="2c6ee7f35c68dbedaff6ef9b6dbf666f")

	depends_on("r@3.3:", type=("build", "run"))
