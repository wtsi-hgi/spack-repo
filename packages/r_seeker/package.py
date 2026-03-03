# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeeker(RPackage):
	"""Simplified Fetching and Processing of Microarray and RNA-Seq
Data

	Wrapper around various existing tools and command-line interfaces,
  providing a standard interface, simple parallelization, and detailed logging.
  For microarray data, maps probe sets to standard gene IDs, building on
  'GEOquery' Davis and Meltzer (2007) <doi:10.1093/bioinformatics/btm254>,
  'ArrayExpress' Kauffmann et al. (2009) <doi:10.1093/bioinformatics/btp354>,
  Robust multi-array average 'RMA' Irizarry et al. (2003) <doi:10.1093/biostatistics/4.2.249>,
  and 'BrainArray' Dai et al. (2005) <doi:10.1093/nar/gni179>.
  For RNA-seq data, fetches metadata and raw reads from National Center for Biotechnology
  Information (NCBI) Sequence Read Archive (SRA), performs standard adapter and
  quality trimming using 'TrimGalore' Krueger <https://github.com/FelixKrueger/TrimGalore>,
  performs quality control checks using 'FastQC' Andrews <https://github.com/s-andrews/FastQC>,
  quantifies transcript abundances using 'salmon' Patro et al. (2017) <doi:10.1038/nmeth.4197> and potentially
  'refgenie' Stolarczyk et al. (2020) <doi:10.1093/gigascience/giz149>,
  aggregates the results using 'MultiQC' Ewels et al. (2016) <doi:10.1093/bioinformatics/btw354>,
  maps transcripts to genes using 'biomaRt' Durinkck et al. (2009) <doi:10.1038/nprot.2009.97>,
  and summarizes transcript-level quantifications for gene-level analyses using
  'tximport' Soneson et al. (2015) <doi:10.12688/f1000research.7563.2>.
	"""
	
	homepage = "https://seeker.hugheylab.org"
	cran = "seeker" 

	version("1.1.5", md5="9dfdb443bdb74adb1688bbd2a4fa9052")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-affy@1.68:", type=("build", "run"))
	depends_on("r-annotationdbi@1.52:", type=("build", "run"))
	depends_on("r-biocmanager@1.30:", type=("build", "run"))
	depends_on("r-biomart@2.36.1:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-curl@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-geoquery@2.58:", type=("build", "run"))
	depends_on("r-glue@1.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-qs@0.21.2:", type=("build", "run"))
	depends_on("r-r-utils@2.11:", type=("build", "run"))
	depends_on("r-rcurl@1.98:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-sessioninfo@1.2:", type=("build", "run"))
	depends_on("r-tximport@1.8:", type=("build", "run"))
	depends_on("r-withr@2.4.2:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
