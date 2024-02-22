# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcauchyd(RPackage):
	"""Multivariate Cauchy Distribution; Kullback-Leibler Divergence

	Distance between multivariate Cauchy distributions, as presented by N. Bouhlel and D. Rousseau (2022) <doi:10.3390/e24060838>. Manipulation of multivariate Cauchy distributions.
	"""
	
	homepage = "https://forgemia.inra.fr/imhorphen/mcauchyd"
	cran = "mcauchyd" 

	version("1.2.0", md5="a0b2322c399e79b4f465c8f675ca154a")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
