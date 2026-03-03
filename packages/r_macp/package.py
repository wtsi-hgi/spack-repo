# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacp(RPackage):
	"""Macromolecular Assemblies from Co-Elution Profile (MACP)

	The MACP employs machine learning algorithm for automated scoring 
   of co-fractionation mass spectrometry (CF-MS) and then systematically 
   map multi-protein complexes from these high-confidence protein-protein 
   interactions (PPIs) using unsupervised learning (i.e., clustering).
	"""
	
	homepage = "https://github.com/mrbakhsh/MACP"
	cran = "MACP" 

	version("0.1.0", md5="1b97ce9d94ed8c334c5f8cae24a4cf78")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
