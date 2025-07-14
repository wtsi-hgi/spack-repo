# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyhgu133plus2expr(RPackage):
	"""Affyhgu133Plus2Expr (GPL570) Expression Data Package

	Contains pre-built human (GPL570) database of gene expression profiles. The gene expression data was downloaded from NCBI GEO and preprocessed and normalized consistently. The biological context of each sample was recorded and manually verified based on the sample description in GEO.
	"""
	
	bioc = "Affyhgu133Plus2Expr" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Affyhgu133Plus2Expr_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Affyhgu133Plus2Expr/Affyhgu133Plus2Expr_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="092e524d019a2b7a9a31821769834a6a5d9928d5b3eff6075148ad5ecca75182")

	depends_on("r@2.10:", type=("build", "run"))

