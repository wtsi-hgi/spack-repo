# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrettyb(RPackage):
	"""Pretty Base Graphics

	Drop-in replacements for standard base graphics
    functions. The replacements are prettier versions of the originals.
	"""
	
	homepage = "https://github.com/jumpingrivers/prettyB/"
	cran = "prettyB" 

	version("0.2.2", md5="3390411da5bb850a17cec25bbca9afce")

