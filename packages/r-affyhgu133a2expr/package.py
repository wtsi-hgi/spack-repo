# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyhgu133a2expr(RPackage):
	"""Affymetrix Human Genome U133A 2.0 Array (GPL571) Expression Data Package

	Contains pre-built human (GPL571) databases of gene expression profiles. The gene expression data was downloaded from NCBI GEO and preprocessed and normalized consistently. The biological context of each sample was recorded and manually verified based on the sample description in GEO.
	"""
	
	bioc = "Affyhgu133A2Expr" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Affyhgu133A2Expr_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Affyhgu133A2Expr/Affyhgu133A2Expr_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="ac2fcf59929091afd1683adf122055ce9df4c5ebc43ba118e9e04b14c70f7ce7")

	depends_on("r@2.10:", type=("build", "run"))

