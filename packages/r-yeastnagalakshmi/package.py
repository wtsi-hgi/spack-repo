# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastnagalakshmi(RPackage):
	"""Yeast genome RNA sequencing data based on Nagalakshmi et. al.

	The yeast genome data was retrieved from the sequence read archive, aligned with bwa, and converted to BAM format with samtools.
	"""
	
	bioc = "yeastNagalakshmi"

	version("1.44.0", commit="9f9f35453f8f5a4d22bd2bbdcbd6358144b3d2f7")
	version("1.38.0", commit="1687f8efcec9452030247e16f9bee4ecec4dd615")


