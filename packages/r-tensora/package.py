# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensora(RPackage):
	"""Advanced Tensor Arithmetic with Named Indices.

	Provides convenience functions for advanced linear algebra with tensors and
	computation with data sets of tensors on a higher level abstraction. It
	includes Einstein and Riemann summing conventions, dragging, co- and
	contravariate indices, parallel computations on sequences of tensors."""

	cran = "tensorA"

	license("GPL-2.0-or-later")

	version("0.36.2.1", md5="262cae742a4518d5e16fd13aa45158cc")

	depends_on("r@2.2:", type=("build", "run"))
