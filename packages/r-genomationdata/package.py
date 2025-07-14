# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomationdata(RPackage):
	"""Experimental data for showing functionalities of the genomation package

	The package contains Chip Seq, Methylation and Cage data, downloaded from Encode
	"""
	
	bioc = "genomationData"

	version("1.40.0", commit="cbaf8648bb999705aff5c29e0ef737de03062211")
	version("1.34.0", commit="3cd09f29a801c8063eb17894016020d9ecf0d5c3")


