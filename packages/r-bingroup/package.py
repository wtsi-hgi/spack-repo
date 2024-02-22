# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBingroup(RPackage):
	"""Evaluation and Experimental Design for Binomial Group Testing

	Methods for estimation and hypothesis testing of proportions
 in group testing designs: methods for estimating a proportion in a single
        population (assuming sensitivity and specificity equal to 1 in designs
        with equal group sizes), as well as hypothesis tests and
        functions for experimental design for this situation. For
        estimating one proportion or the difference of proportions, a
        number of confidence interval methods are included, which can
        deal with various different pool sizes. Further, regression
        methods are implemented for simple pooling and matrix pooling
        designs.
        Methods for identification of positive items in group
        testing designs: Optimal testing configurations can be found 
        for hierarchical and array-based algorithms. Operating 
        characteristics can be calculated for testing configurations 
        across a wide variety of situations.
	"""
	
	cran = "binGroup" 

	version("2.2-1", md5="430aa715a1c8986788c28010e7f0f7e5")

	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
