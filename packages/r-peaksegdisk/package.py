# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeaksegdisk(RPackage):
	"""Disk-Based Constrained Change-Point Detection

	Disk-based implementation of
 Functional Pruning Optimal Partitioning with up-down constraints
 <doi:10.18637/jss.v101.i10> for single-sample peak calling
 (independently for each sample and genomic problem),
 can handle huge data sets (10^7 or more).
	"""
	
	homepage = "https://github.com/tdhock/PeakSegDisk"
	cran = "PeakSegDisk" 

	version("2023.11.27", md5="88362e5251c1f6598fbe130efca940c2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
