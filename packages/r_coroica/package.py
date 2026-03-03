# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoroica(RPackage):
	"""Confounding Robust Independent Component Analysis for Noisy and
Grouped Data

	Contains an implementation of a confounding robust independent component analysis (ICA) for noisy and grouped data. The main function coroICA() performs a blind source separation, by maximizing an independence across sources and allows to adjust for varying confounding based on user-specified groups. Additionally, the package contains the function uwedge() which can be used to approximately jointly diagonalize a list of matrices. For more details see the project website <https://sweichwald.de/coroICA/>.
	"""
	
	homepage = "https://github.com/sweichwald/coroICA-R"
	cran = "coroICA" 

	version("1.0.2", md5="add5096af5efa638e2b7bee584602e45")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
