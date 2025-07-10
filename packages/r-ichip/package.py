# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIchip(RPackage):
	"""Bayesian Modeling of ChIP-chip Data Through Hidden Ising Models

	Hidden Ising models are implemented to identify enriched genomic regions in ChIP-chip data.  They can be used to analyze the data from multiple platforms (e.g., Affymetrix, Agilent, and NimbleGen), and the data with single to multiple replicates.
	"""
	
	bioc = "iChip" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iChip_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iChip/iChip_1.56.0.tar.gz"]

	version("1.56.0", sha256="fef7eb975b3d6ae17f73246b50c03f35aea19be394906eadd4b526e41da3e51f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
