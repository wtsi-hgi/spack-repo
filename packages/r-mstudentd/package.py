# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstudentd(RPackage):
	"""Multivariate t Distribution

	Distance between multivariate t distributions, as presented by N. Bouhlel and D. Rousseau (2023) <doi:10.1109/LSP.2023.3324594>.
	"""
	
	homepage = "https://forgemia.inra.fr/imhorphen/mstudentd"
	cran = "mstudentd" 

	version("1.0.0", md5="267f6c3c90712db53200083cfacf30c0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
