# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatUtils(RPackage):
	"""File System Utility Functions for 'NeuroAnatomy Toolbox'

	Utility functions that may be of general interest
    but are specifically required by the 'NeuroAnatomy Toolbox' ('nat').
    Includes functions to provide a basic make style system to update
    files based on timestamp information, file locking and 'touch'
    utility. Convenience functions for working with file paths include
    'abs2rel', 'split_path' and 'common_path'. Finally there are utility
    functions for working with 'zip' and 'gzip' files including integrity
    tests.
	"""
	
	homepage = "https://github.com/natverse/nat.utils"
	cran = "nat.utils" 

	version("0.6.1", md5="7d698bccb1fcb5104269e9246c20e763")

	depends_on("r-checkmate", type=("build", "run"))
