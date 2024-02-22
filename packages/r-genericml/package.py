# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenericml(RPackage):
	"""Generic Machine Learning Inference

	Generic Machine Learning Inference on heterogeneous treatment effects in randomized experiments as proposed in Chernozhukov, Demirer, Duflo and Fernández-Val (2020) <arXiv:1712.04802>. This package's workhorse is the 'mlr3' framework of Lang et al. (2019) <doi:10.21105/joss.01903>, which enables the specification of a wide variety of machine learners. The main functionality, GenericML(), runs Algorithm 1 in Chernozhukov, Demirer, Duflo and Fernández-Val (2020) <arXiv:1712.04802> for a suite of user-specified machine learners. All steps in the algorithm are customizable via setup functions. Methods for printing and plotting are available for objects returned by GenericML(). Parallel computing is supported.
	"""
	
	homepage = "https://github.com/mwelz/GenericML/"
	cran = "GenericML" 

	version("0.2.2", md5="6901f999b3dc93a46b08bfc16c6c8d24")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-mlr3learners", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
