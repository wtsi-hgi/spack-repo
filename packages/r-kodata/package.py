# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKodata(RPackage):
	"""LINCS Knock-Out Data Package

	Contains consensus genomic signatures (CGS) for experimental cell-line specific gene knock-outs as well as baseline gene expression data for a subset of experimental cell-lines. Intended for use with package KEGGlincs.
	"""
	
	bioc = "KOdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/KOdata_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/KOdata/KOdata_1.28.0.tar.gz"]

	version("1.28.0", md5="40e099053eae889ad66256a94427ac54")

	depends_on("r@3.3:", type=("build", "run"))

	# experiment