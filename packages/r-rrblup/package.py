# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrblup(RPackage):
	"""Ridge Regression and Other Kernels for Genomic Selection.

	Software for genomic prediction with the RR-BLUP mixed model (Endelman
	2011, <doi:10.3835/plantgenome2011.08.0024>). One application is to
	estimate marker effects by ridge regression; alternatively, BLUPs can be
	calculated based on an additive relationship matrix or a Gaussian
	kernel."""

	cran = "rrBLUP"

	version("4.6.3", md5="d0ca5c34c12d7729390bdb00cbaa24a4")

	depends_on("r@4:", type=("build", "run"))
