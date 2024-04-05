# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscmt(RPackage):
	"""Multivariate Synthetic Control Method Using Time Series

	Three generalizations of the synthetic control method (which has 
    already an implementation in package 'Synth') are implemented: first, 
    'MSCMT' allows for using multiple outcome variables, second, time series 
    can be supplied as economic predictors, and third, a well-defined 
    cross-validation approach can be used.
    Much effort has been taken to make the implementation as stable as possible 
    (including edge cases) without losing computational efficiency.
    A detailed description of the main algorithms is given in 
    Becker and Klößner (2018) <doi:10.1016/j.ecosta.2017.08.002>.
	"""
	
	cran = "MSCMT" 

	version("1.4.0", md5="007ab0a5fbfe6cc29bbdb59f88b216db")
	version("1.3.9", md5="2f2e94b2d5838173d1c3a0c3032b9e42")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
