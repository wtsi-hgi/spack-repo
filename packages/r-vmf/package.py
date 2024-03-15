# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVmf(RPackage):
	"""Sampling from the von Mises-Fisher Distribution

	Provides fast sampling from von Mises-Fisher distribution using the method proposed by Andrew T.A Wood (1994) <doi:10.1080/03610919408813161>.
	"""
	
	homepage = "https://github.com/ahoundetoungan/vMF"
	cran = "vMF" 

	version("0.0.3", md5="f27b4dc94694a319be56b7ea334a3eed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
