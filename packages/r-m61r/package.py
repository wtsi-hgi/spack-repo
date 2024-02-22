# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM61r(RPackage):
	"""Package About Data Manipulation in Pure Base R

	Data manipulation in one package and in base R.
  Minimal. No dependencies.
  'dplyr' and 'tidyr'-like in one place.
  Nothing else than base R to build the package.
	"""
	
	homepage = "https://github.com/pv71u98h1/m61r/"
	cran = "m61r" 

	version("0.0.3", md5="bd860106c50b440f67d6ef2614785611")

	depends_on("r@3.4.4:", type=("build", "run"))
