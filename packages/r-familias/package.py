# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamilias(RPackage):
	"""Probabilities for Pedigrees Given DNA Data

	An interface to the core 'Familias' functions which are
    programmed in C++. The implementation is described in Egeland, Mostad and Olaisen
    (1997) <doi:10.1016/S1355-0306(97)72202-0> and Simonsson and Mostad
    (2016) <doi:10.1016/j.fsigen.2016.04.005>.
	"""
	
	homepage = "https://www.familias.name/openfamilias.html"
	cran = "Familias" 

	version("2.6.1", md5="c82d2a78527f8f78c21732dedc7bcaaa")

	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
