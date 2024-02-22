# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRt3(RPackage):
	"""Tic-Tac-Toe Package for R

	Play the classic game of tic-tac-toe (naughts and crosses).
	"""
	
	cran = "rt3" 

	version("0.1.2", md5="d085cbb888acf1ec10b30d19b36872b7", url="https://cran.r-project.org/src/contrib/rt3_0.1.2.tar.gz")

