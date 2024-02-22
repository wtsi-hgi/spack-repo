# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTunepareto(RPackage):
	"""Multi-Objective Parameter Tuning for Classifiers

	Generic methods for parameter tuning of classification algorithms using multiple scoring functions (Muessel et al. (2012), <doi:10.18637/jss.v046.i05>).
	"""
	
	cran = "TunePareto" 

	version("2.5.3", md5="77a5e561d65347c891442ba2f50e2f7d")

