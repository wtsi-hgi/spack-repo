# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernsmooth(RPackage):
	"""Functions for Kernel Smoothing Supporting Wand & Jones (1995).

	Functions for kernel smoothing (and density estimation) corresponding to
	the book:  Wand, M.P. and Jones, M.C. (1995) "Kernel Smoothing"."""

	cran = "KernSmooth"

	version("2.23-22", md5="88c17e2ef6dc2315d5288b23adee5bf3")

	depends_on("r@2.5:", type=("build", "run"))
