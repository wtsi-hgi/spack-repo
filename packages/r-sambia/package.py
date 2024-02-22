# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSambia(RPackage):
	"""A Collection of Techniques Correcting for Sample Selection Bias

	A collection of various techniques correcting statistical models for sample selection bias is provided. In particular, the resampling-based methods "stochastic inverse-probability oversampling" and "parametric inverse-probability bagging" are placed at the disposal which generate synthetic observations for correcting classifiers for biased samples resulting from stratified random sampling. For further information, see the article Krautenbacher, Theis, and Fuchs (2017) <doi:10.1155/2017/7847531>. The methods may be used for further purposes where weighting and generation of new observations is needed.
	"""
	
	cran = "sambia" 

	version("0.1.0", md5="b9e862f3d25633deb8e8abb432ff57ef")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
