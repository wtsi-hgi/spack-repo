# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixreg(RPackage):
	"""Functions to Fit Mixtures of Regressions

	Fits mixtures of (possibly multivariate) regressions
	(which has been described as doing ANCOVA when you don't
	know the levels). Turner (2000) <doi:10.1111/1467-9876.00198>.
	"""
	
	homepage = "http://www.stat.auckland.ac.nz/~rolf/"
	cran = "mixreg" 

	version("2.0-10", md5="596bf71256d16893a38cf3d4ba010c16")

	depends_on("r@3.5:", type=("build", "run"))
