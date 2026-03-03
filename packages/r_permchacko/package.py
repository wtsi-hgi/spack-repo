# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermchacko(RPackage):
	"""Chacko Test for Order-Restriction with Permutation

	Implements an extension of the Chacko chi-square test for
    ordered vectors (Chacko, 1966, <https://www.jstor.org/stable/25051572>).
    Our extension brings the Chacko test to the computer age by implementing
    a permutation test to offer a numeric estimate of the p-value, which is
    particularly useful when the analytic solution is not available.
	"""
	
	homepage = "https://ocbe-uio.github.io/permChacko/"
	cran = "permChacko" 

	version("0.2.0", md5="621803422e8d6e25f6d35eb8fe561bef")

