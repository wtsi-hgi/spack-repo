# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlf(RPackage):
	"""Machine Learning Foundations

	Offers a gentle introduction to machine learning concepts for practitioners with a statistical pedigree: decomposition of model error (bias-variance trade-off), nonlinear correlations, information theory and functional permutation/bootstrap simulations. Székely GJ, Rizzo ML, Bakirov NK. (2007). <doi:10.1214/009053607000000505>. Reshef DN, Reshef YA, Finucane HK, Grossman SR, McVean G, Turnbaugh PJ, Lander ES, Mitzenmacher M, Sabeti PC. (2011). <doi:10.1126/science.1205438>.
	"""
	
	homepage = "http://mlf-project.us/"
	cran = "mlf" 

	version("1.2.1", md5="acd7a9f2b2e9e94db0d6347e94dad1cc")

