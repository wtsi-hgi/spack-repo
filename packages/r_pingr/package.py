# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPingr(RPackage):
	"""Check if a Remote Computer is Up

	Check if a remote computer is up. It can either just call the
    system ping command, or check a specified TCP port.
	"""
	
	homepage = "https://r-lib.github.io/pingr/"
	cran = "pingr" 

	version("2.0.3", md5="1fa6ce8bcbbeda3df39c59180a3ad149")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
