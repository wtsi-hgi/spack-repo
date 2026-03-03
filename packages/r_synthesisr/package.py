# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynthesisr(RPackage):
	"""Import, Assemble, and Deduplicate Bibliographic Datasets

	A critical first step in systematic literature reviews
  and mining of academic texts is to identify relevant texts from a range
  of sources, particularly databases such as 'Web of Science' or 'Scopus'.
  These databases often export in different formats or with different metadata
  tags. 'synthesisr' expands on the tools outlined by Westgate (2019)
  <doi:10.1002/jrsm.1374> to import bibliographic data from a range of formats
  (such as 'bibtex', 'ris', or 'ciw') in a standard way, and allows merging
  and deduplication of the resulting dataset.
	"""
	
	cran = "synthesisr" 

	version("0.3.0", md5="78b408cd4c2b3e612a0a58f64b2c8c1e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
