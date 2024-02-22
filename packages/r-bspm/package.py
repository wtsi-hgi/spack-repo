# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBspm(RPackage):
	"""Bridge to System Package Manager

	Enables binary package installations on Linux distributions.
    Provides functions to manage packages via the distribution's package
    manager. Also provides transparent integration with R's install.packages()
    and a fallback mechanism. When installed as a system package, interacts
    with the system's package manager without requiring administrative
    privileges via an integrated D-Bus service; otherwise, uses sudo.
    Currently, the following backends are supported: DNF, APT, ALPM.
	"""
	
	homepage = "https://enchufa2.github.io/bspm/"
	cran = "bspm" 

	version("0.5.5", md5="86d4bc20c4b90d6d61873e554e0a20f4")

