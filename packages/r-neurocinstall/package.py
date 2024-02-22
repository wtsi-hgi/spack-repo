# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeurocinstall(RPackage):
	"""'Neuroconductor' Installer

	Installs 'Neuroconductor' packages from the release repository <https://neuroconductor.org/releases/> or from 'GitHub'.
	"""
	
	cran = "neurocInstall" 

	version("0.12.0", md5="e86a370f524edfa50fdc4675ef9ee4bc")

	depends_on("r-devtools@1.12.0.9000:", type=("build", "run"))
