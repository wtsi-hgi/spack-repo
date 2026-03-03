# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCla(RPackage):
	"""Critical Line Algorithm in Pure R

	Implements 'Markowitz' Critical Line Algorithm ('CLA') for classical
  mean-variance portfolio optimization, see Markowitz (1952) <doi:10.2307/2975974>.
  Care has been taken for correctness in light of previous buggy implementations.
	"""
	
	homepage = "https://gitlab.math.ethz.ch/maechler/CLA/"
	cran = "CLA" 

	version("0.96-2", md5="14e915becc93b9cc346b4470f37ecbf7")

	depends_on("r@3.6:", type=("build", "run"))
