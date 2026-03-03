# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxalight(RPackage):
	"""A Lightweight and Lightning-Fast Taxonomic Naming Interface

	Creates a local Lightning Memory-Mapped Database ('LMDB') 
             of many commonly used taxonomic authorities
             and provides functions that can quickly query this data.
             Supported taxonomic authorities include 
             the Integrated Taxonomic Information System ('ITIS'),
             National Center for Biotechnology Information ('NCBI'),
             Global Biodiversity Information Facility ('GBIF'), 
             Catalogue of Life ('COL'), and Open Tree Taxonomy ('OTT'). 
             Name and identifier resolution using 'LMDB' can
             be hundreds of times faster than either relational databases or
             internet-based queries. Precise data provenance information for
             data derived from naming providers is also included.
	"""
	
	homepage = "https://github.com/cboettig/taxalight"
	cran = "taxalight" 

	version("0.1.5", md5="623f506bb4f64a9f0a72404a5dc0b942")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-thor", type=("build", "run"))
	depends_on("r-contentid", type=("build", "run"))
