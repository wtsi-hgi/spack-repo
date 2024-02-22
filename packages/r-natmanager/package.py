# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatmanager(RPackage):
	"""Install the 'Natverse' Packages from Scratch

	Provides streamlined installation for packages from the 'natverse',
    a suite of R packages for computational neuroanatomy built on top of the
    'nat' 'NeuroAnatomy Toolbox' package. Installation of the complete
    'natverse' suite requires a 'GitHub' user account and personal access token
    'GITHUB_PAT'. 'natmanager' will help the end user set this up if necessary.
	"""
	
	homepage = "https://github.com/natverse/natmanager"
	cran = "natmanager" 

	version("0.5.1", md5="7128c3213631e0e37fdcb35adbe21bd5")

	depends_on("r-gh@1.2.1:", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-pak", type=("build", "run"))
	depends_on("r-usethis@2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
