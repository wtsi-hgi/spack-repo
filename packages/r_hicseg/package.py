# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicseg(RPackage):
	"""Detection of domains in HiC data

	This package allows you to detect domains in HiC data by rephrasing this problem as a two-dimensional segmentation issue.
	"""
	
	cran = "HiCseg" 

	version("1.1", md5="38e211ee2c32384a4c2b19f1ec986f51")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
