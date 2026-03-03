# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistro(RPackage):
	"""Linux Distribution Properties

	In order to provide unified access to Linux distribution details
    in R, this package wraps the various files and commands that may exist
    on a system. It is similar in spirit to the 'lsb_release' command and the
    'Python' package of the same name.
	"""
	
	cran = "distro" 

	version("0.1.0", md5="93f9a58fa0151253b71e447cffd19afa")

