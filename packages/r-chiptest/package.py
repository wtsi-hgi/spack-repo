# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChiptest(RPackage):
	"""Nonparametric Methods for Identifying Differential Enrichment
Regions with ChIP-Seq Data

	Nonparametric Tests to identify the differential enrichment region for two conditions or time-course ChIP-seq data. It includes: data preprocessing function, estimation of a small constant used in hypothesis testing, a kernel-based two sample nonparametric test, two assumption-free  two sample nonparametric test.
	"""
	
	cran = "ChIPtest" 

	version("1.0", md5="97ae51d6743a3a0da6b10b10d9bbe2b7")

