# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWperm(RPackage):
	"""Permutation Tests

	Supplies permutation-test alternatives to traditional hypothesis-test
  procedures such as two-sample tests for means, medians, and standard deviations;
  correlation tests; tests for homogeneity and independence; and more. Suitable for
  general audiences, including individual and group users, introductory statistics
  courses, and more advanced statistics courses that desire an introduction to
  permutation tests.
	"""
	
	cran = "wPerm" 

	version("1.0.1", md5="3de68fc8b2fd9b5133210666c754ca12")

	depends_on("r@3.1:", type=("build", "run"))
