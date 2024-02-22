# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDigitalpcr(RPackage):
	"""Estimate Copy Number for Digital PCR

	The assay sensitivity is the minimum number of copies that the digital PCR assay can detect. Users provide serial dilution results in the format of counts of positive and total reaction wells. The output is the estimated assay sensitivity and the copy number per well in the initial dilute.
	"""
	
	cran = "digitalPCR" 

	version("1.1.0", md5="857d1d898f8d41e27e06e5a18c2a834e")

