# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPracpac(RPackage):
	"""Practical 'R' Packaging in 'Docker'

	Streamline the creation of 'Docker' images with 'R' packages and dependencies embedded. The 'pracpac' package provides a 'usethis'-like interface to creating Dockerfiles with dependencies managed by 'renv'. The 'pracpac' functionality is described in Nagraj and Turner (2023) <doi:10.48550/arXiv.2303.07876>.
	"""
	
	homepage = "https://signaturescience.github.io/pracpac/"
	cran = "pracpac" 

	version("0.2.0", md5="bd8e14f5bbb4845674b89f4a3a55b6ad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
