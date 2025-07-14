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

	version("1.46.0", commit="50eda27682cb98293e6576208be478c4bb80ea8a")
	version("1.40.0", commit="9f25e5a3cb70a657402a611c18c0210136e8af21")

	depends_on("r@2.10:", type=("build", "run"))

