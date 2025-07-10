# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetapone(RPackage):
	"""Conducts pathway test of metabolomics data using a weighted permutation test

	The package conducts pathway testing from untargetted metabolomics data. It requires the user to supply feature-level test results, from case-control testing, regression, or other suitable feature-level tests for the study design. Weights are given to metabolic features based on how many metabolites they could potentially match to. The package can combine positive and negative mode results in pathway tests.
	"""
	
	bioc = "metapone" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metapone_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metapone/metapone_1.8.0.tar.gz"]

	version("1.8.0", sha256="4f660792fb1420623fa383a952b10ebec5231d7776c4581b7e50403f9d440390")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
