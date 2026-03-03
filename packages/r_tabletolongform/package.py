# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabletolongform(RPackage):
	"""Automatically Convert Hierarchical for-Human Tables to
Machine-Readable LongForm Dataframes

	A wrapper to a set of algorithms designed to recognise positional cues present in hierarchical for-human Tables (which would normally be interpreted visually by the human brain) to decompose, then reconstruct the data into machine-readable LongForm Dataframes.
	"""
	
	homepage = "https://www.stat.auckland.ac.nz/~joh024/Research/TableToLongForm/"
	cran = "TableToLongForm" 

	version("1.3.2", md5="414e6e938698f6f6ebc4f077bab5639e")

