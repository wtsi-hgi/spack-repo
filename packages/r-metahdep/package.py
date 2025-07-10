# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetahdep(RPackage):
	"""Hierarchical Dependence in Meta-Analysis

	Tools for meta-analysis in the presence of hierarchical (and/or sampling) dependence, including with gene expression studies
	"""
	
	bioc = "metahdep" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metahdep_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metahdep/metahdep_1.60.0.tar.gz"]

	version("1.60.0", sha256="fba9b055ecbf7ccc142946adf47634d505ef1baae3a640f89f0db094da0fa941")

	depends_on("r@2.10:", type=("build", "run"))
