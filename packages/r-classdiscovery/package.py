# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassdiscovery(RPackage):
	"""Classes and Methods for "Class Discovery" with Microarrays or
Proteomics

	Defines the classes used for "class discovery" problems
  in the OOMPA project (<http://oompa.r-forge.r-project.org/>). Class
  discovery primarily consists of unsupervised clustering methods with
  attempts to assess their statistical significance. 
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "ClassDiscovery" 

	version("3.4.0", md5="fea0ddc09b772d6abc0f0eaf9bf86473")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-oompabase@3.0.1:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-oompadata", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
