# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRotor(RPackage):
	"""Log Rotation and Conditional Backups

	Conditionally rotate or back-up files based on
    their size or the date of the last backup; inspired by the 'Linux'
    utility 'logrotate'.
	"""
	
	homepage = "https://s-fleck.github.io/rotor/"
	cran = "rotor" 

	version("0.3.7", md5="a38f7ab209f9e09e53ff44ef29b56c4b")

	depends_on("r-dint", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
