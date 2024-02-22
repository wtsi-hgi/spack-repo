# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmaspu(RPackage):
	"""An Adaptive Test on High Dimensional Parameters in Generalized
Linear Models

	Several tests for high dimensional generalized linear models have been proposed recently. In this package, we implemented a new test called adaptive  sum of powered score (aSPU) for high dimensional generalized linear models, which is often more powerful than the existing methods in a wide scenarios. We also implemented permutation based version of several existing methods for research purpose. We recommend users use the aSPU test for their real testing problem. You can learn more about the tests implemented in the package via the following papers: 1. Pan, W., Kim, J., Zhang, Y., Shen, X. and Wei, P. (2014) <DOI:10.1534/genetics.114.165035> A powerful and adaptive association test for rare variants, Genetics, 197(4). 2. Guo, B., and Chen, S. X. (2016) <DOI:10.1111/rssb.12152>. Tests for high dimensional generalized linear models. Journal of the Royal Statistical Society: Series B. 3. Goeman, J. J., Van Houwelingen, H. C., and Finos, L. (2011) <DOI:10.1093/biomet/asr016>. Testing against a high-dimensional alternative in the generalized linear model: asymptotic type I error control. Biometrika, 98(2).
	"""
	
	cran = "GLMaSPU" 

	version("1.0", md5="815e44fc07e1a93db5a737c4fc76f7f9")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
