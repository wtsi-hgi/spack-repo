# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbati(RPackage):
	"""Gene by Environment Interaction and Conditional Gene Tests for
Nuclear Families

	Does family-based gene by environment interaction tests, joint gene, gene-environment interaction test, and a test of a set of genes conditional on another set of genes.
	"""
	
	homepage = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3120904/"
	cran = "fbati" 

	version("1.0-9", md5="e21522569f62f6c8cc2bca6e3f89f7a3")

	depends_on("r-pbatr@2.2.17:", type=("build", "run"))
	depends_on("r-fgui", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
