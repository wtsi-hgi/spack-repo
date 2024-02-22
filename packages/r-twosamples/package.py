# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwosamples(RPackage):
	"""Fast Permutation Based Two Sample Tests

	Fast randomization based two sample tests. 
  Testing the hypothesis that two samples come from the same distribution using randomization to create p-values. Included tests are: Kolmogorov-Smirnov, Kuiper, Cramer-von Mises, Anderson-Darling, Wasserstein, and DTS. The default test (two_sample) is based on the DTS test statistic, as it is the most powerful, and thus most useful to most users. 
  The DTS test statistic builds on the Wasserstein distance by using a weighting scheme like that of Anderson-Darling. See the companion paper at <arXiv:2007.01360> or <https://codowd.com/public/DTS.pdf> for details of that test statistic, and non-standard uses of the package (parallel for big N, weighted observations, one sample tests, etc). We also include the permutation scheme to make test building simple for others.
	"""
	
	homepage = "https://twosampletest.com"
	cran = "twosamples" 

	version("2.0.1", md5="9b2d929b38404c51a72fd50853b6f758")

	depends_on("r-cpp11", type=("build", "run"))
