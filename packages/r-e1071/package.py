# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RE1071(RPackage):
	"""Misc Functions of the Department of Statistics, Probability Theory Group
	(Formerly: E1071), TU Wien.

	Functions for latent class analysis, short time Fourier transform, fuzzy
	clustering, support vector machines, shortest path computation, bagged
	clustering, naive Bayes classifier, generalized k-nearest neighbour ..."""

	cran = "e1071"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("1.7-14", md5="03776052baef3f5e7cf8ccc1e493cfb2", url="https://cran.r-project.org/src/contrib/e1071_1.7-14.tar.gz")

	depends_on("r-class", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
