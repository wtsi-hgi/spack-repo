# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitr(RPackage):
	"""A Lightweight API for 'Git'

	A light-weight, dependency-free, application programming interface
    (API) to access system-level 'Git' commands from within 'R'. Contains wrappers
    and defaults for common data science workflows as well as
    'Zsh' plugin aliases. A generalized API syntax is also available.
    A system installation of 'Git' <https://git-scm.com/downloads> is required.
	"""
	
	homepage = "https://stufield.github.io/gitr/"
	cran = "gitr" 

	version("0.0.1", md5="65c6c2cb731b9ea579836271ab322540")

	depends_on("r@4.1:", type=("build", "run"))
