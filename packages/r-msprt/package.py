# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsprt(RPackage):
	"""A Modified Sequential Probability Ratio Test (MSPRT)

	Given the maximum available sample size (N) for an experiment, and the target levels of Type I 
             and II error probabilities, this package designs a modified SPRT (MSPRT). For any designed MSPRT 
             the package can also obtain its operating characteristics and implement the test for a given 
             sequentially observed data. The MSPRT is defined in a manner very similar to Wald's initial proposal. 
             The proposed test has shown evidence of reducing the average sample size required to perform 
             statistical hypothesis tests at specified levels of significance and power. Currently, the package
             implements one-sample proportion tests, one and two-sample z tests, and one and two-sample 
             t tests. A brief user guidance for this package is provided below. One can also refer to the 
             supplemental information for the same.
	"""
	
	cran = "MSPRT" 

	version("3.0", md5="81e6dac0d00392759355dda772ac04aa")

	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
