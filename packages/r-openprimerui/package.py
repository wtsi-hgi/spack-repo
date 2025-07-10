# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenprimerui(RPackage):
	"""Shiny Application for Multiplex PCR Primer Design and Analysis

	A Shiny application providing methods for designing, evaluating, and comparing primer sets for multiplex polymerase chain reaction. Primers are designed by solving a set cover problem such that the number of covered template sequences is maximized with the smallest possible set of primers. To guarantee that high-quality primers are generated, only primers fulfilling constraints on their physicochemical properties are selected.
	"""
	
	bioc = "openPrimeRui" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/openPrimeRui_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/openPrimeRui/openPrimeRui_1.24.0.tar.gz"]

	version("1.24.0", sha256="34b6ea9cbdc6f65ee90984cabc1a0f928f0309a82e09e7d4354dc0fec98fd5ef")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-openprimer@0.99:", type=("build", "run"))
	depends_on("r-shiny@1.0.2:", type=("build", "run"))
	depends_on("r-shinyjs@0.9:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-rmarkdown@1:", type=("build", "run"))
