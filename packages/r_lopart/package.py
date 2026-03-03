# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLopart(RPackage):
	"""Labeled Optimal Partitioning

	Change-point detection algorithm with
 label constraints and a penalty for each change outside of labels.
 Read TD Hocking, A Srivastava (2020) <arXiv:2006.13967> for details.
	"""
	
	homepage = "https://github.com/tdhock/LOPART"
	cran = "LOPART" 

	version("2020.6.29", md5="b5cfa1687a562b57ced0b5f653222d69")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
