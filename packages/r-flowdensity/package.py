# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowdensity(RPackage):
	"""Sequential Flow Cytometry Data Gating

	This package provides tools for automated sequential gating analogous to the manual gating strategy based on the density of the data.
	"""
	
	bioc = "flowDensity" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowDensity_1.36.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowDensity/flowDensity_1.36.1.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.1", sha256="e2b9102bc7c67cd450d340602fc88d2ef8736266b7ff9386974192fae6d65570")

	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz@1.42:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-polyclip", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
