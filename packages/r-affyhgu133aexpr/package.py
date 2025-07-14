# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyhgu133aexpr(RPackage):
	"""Affymetrix Human hgu133a Array (GPL96) Expression Data Package

	Contains pre-built human (GPL96) database of gene expression profiles. The gene expression data was downloaded from NCBI GEO, preprocessed and normalized consistently. The biological context of each sample was recorded and manually verified based on the sample description in GEO.
	"""
	
	bioc = "Affyhgu133aExpr" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Affyhgu133aExpr_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Affyhgu133aExpr/Affyhgu133aExpr_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="4e1d08c9eee030971ddacffba4c3ef8da49f1705156372f958b20c2d661ab7cd")

	depends_on("r@2.10:", type=("build", "run"))

