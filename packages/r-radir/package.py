# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadir(RPackage):
	"""Inverse-Regression Estimation of Radioactive Doses

	Radioactive doses estimation using individual chromosomal aberrations information. See Higueras M, Puig P, Ainsbury E, Rothkamm K. (2015) <doi:10.1088/0952-4746/35/3/557>.
	"""
	
	cran = "radir" 

	version("1.0.4", md5="7932db8d96f73a9d9ebbfd2e55c0fb6b")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-hermite", type=("build", "run"))
