# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffymoe4302expr(RPackage):
	"""Affymetrix Mouse Genome 430 2.0 Array (GPL1261) Expression Data Package

	Contains pre-built mouse (GPL1261) database of gene expression profiles. The gene expression data was downloaded from NCBI GEO, preprocessed and normalized consistently. The biological context of each sample was recorded and manually verified based on the sample description in GEO.
	"""
	
	bioc = "Affymoe4302Expr"

	version("1.46.0", commit="dc720b5870152b4f0302d5b773c968cb093133af")
	version("1.40.0", commit="ecfdd0d4173cd25e8edd54c1402a0b3ba941caf1")

	depends_on("r@2.10:", type=("build", "run"))

