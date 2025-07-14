# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRat2302frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type rat2302rnentrezg

	This package was created with the help of frmaTools version 1.24.0.
	"""
	
	bioc = "rat2302frmavecs"

	version("0.99.11", commit="68b05d4e7a78172acddcdaabc60f049acb59fbb0")
	version("0.99.11", commit="68b05d4e7a78172acddcdaabc60f049acb59fbb0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-frma", type=("build", "run"))

