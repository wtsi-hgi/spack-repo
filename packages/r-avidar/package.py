# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvidar(RPackage):
	"""A Computational Biologist’s Toolkit To Get Data From 'avidaDB'

	Easy-to-use tools for performing complex queries on 'avidaDB', a
  semantic database that stores genomic and transcriptomic data of
  self-replicating computer programs (known as digital organisms) that mutate
  and evolve within a user-defined computational environment.
	"""
	
	homepage = "https://gitlab.com/fortunalab/avidaR"
	cran = "avidaR" 

	version("1.2.0", md5="d2b296811888501b4864c65b46842f67")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-tibble@3.0.6:", type=("build", "run"))
	depends_on("r-circlize@0.4.11:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-curl@5.0.2:", type=("build", "run"))
