# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimx(RPackage):
	"""Expanded Replacement and Extension of the 'optim' Function.

	Provides a replacement and extension of the optim() function to call to
	several function minimization codes in R in a single statement. These
	methods handle smooth, possibly box constrained functions of several or
	many parameters. Note that function 'optimr()' was prepared to simplify the
	incorporation of minimization codes going forward. Also implements some
	utility codes and some extra solvers, including safeguarded Newton methods.
	Many methods previously separate are now included here. This is the version
	for CRAN."""

	cran = "optimx"

	license("GPL-2.0-only")

	version("2023-10.21", md5="6bf0366c13fec66c2c89c848ad3fd9b2")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
