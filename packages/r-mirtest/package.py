# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirtest(RPackage):
	"""Combined miRNA- And mRNA-Testing

	Package for combined miRNA- and mRNA-testing.
	"""
	
	homepage = "https://pubmed.ncbi.nlm.nih.gov/22723856/"
	cran = "miRtest" 

	version("2.1", md5="35041de3e7e57cf21c697670839fe24b")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-globaltest", type=("build", "run"))
	depends_on("r-globalancova", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
