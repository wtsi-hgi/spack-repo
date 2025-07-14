# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeaddatapackr(RPackage):
	"""Compression of Illumina BeadArray data

	Provides functionality for the compression and decompression of raw bead-level data from the Illumina BeadArray platform.
	"""
	
	bioc = "BeadDataPackR"

	version("1.60.0", commit="32bd38e6f7f6029d943d29001dd3818e2a562ed1")
	version("1.54.0", commit="71799576f19c9e15024f274d1289d3d386c265d4")

