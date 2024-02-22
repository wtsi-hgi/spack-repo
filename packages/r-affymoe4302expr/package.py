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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Affymoe4302Expr_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/Affymoe4302Expr/Affymoe4302Expr_1.40.0.tar.gz"]

	version("1.40.0", md5="4dcd432d350cf2f8000f67774d95481c")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment