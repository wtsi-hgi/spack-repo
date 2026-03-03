# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJustInstall(RPackage):
	"""Very Simple Function to Install Packages without Attaching

	Install packages without attaching them. If a package it is already installed, it will be skipped.
	"""
	
	cran = "just.install" 

	version("1.0.2", md5="cd20f3a0d6c263235094dc47c4a1f5cd")

	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
