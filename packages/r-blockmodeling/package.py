# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockmodeling(RPackage):
	"""Generalized and Classical Blockmodeling of Valued Networks.

	This is primarily meant as an implementation of generalized blockmodeling
	for valued networks."""

	cran = "blockmodeling"

	license("GPL-2.0-or-later")

	version("1.1.5", md5="58c7580702e7f216874c71bcb94cbdce")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
