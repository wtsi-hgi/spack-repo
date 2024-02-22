# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynsim(RPackage):
	"""Dynamic Simulations of Autoregressive Relationships

	Dynamic simulations and graphical depictions of autoregressive
    relationships.
	"""
	
	homepage = "https://cran.r-project.org/package=dynsim"
	cran = "dynsim" 

	version("1.2.3", md5="2b42197cfe69e6ef224e32ecc15a8682")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1.9003:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
