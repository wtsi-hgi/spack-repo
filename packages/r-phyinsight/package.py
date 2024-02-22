# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyinsight(RPackage):
	"""DNA Sequence Analysis & Generation Tree Creation

	Provide insights using automated DNA sequence manipulation and tree creation. Currently, the package exclusively retrieves data from the BOLD System database (<http://v4.boldsystems.org/index.php/api_home>).
	"""
	
	homepage = "https://jamesc845.github.io/PhyInsight/"
	cran = "PhyInsight" 

	version("0.1.0", md5="560ef7c15d0e3cdaf5127f95363f731a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bold", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-decipher", type=("build", "run"))
