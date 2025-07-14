# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenarise(RPackage):
	"""Microarray Analysis tool

	genArise is an easy to use tool for dual color microarray data. Its GUI-Tk based environment let any non-experienced user performs a basic, but not simple, data analysis just following a wizard. In addition it provides some tools for the developer.
	"""
	
	homepage = "http://www.ifc.unam.mx/genarise"
	bioc = "genArise" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/genArise_1.78.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/genArise/genArise_1.78.0.tar.gz"]

	version("1.84.0", tag="RELEASE_3_21")
	version("1.78.0", sha256="e095e1c32a8eac4d36e7a5387e86b03a23d65e24234967e3f72387ec9a7e6199")

	depends_on("r@1.7.1:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
