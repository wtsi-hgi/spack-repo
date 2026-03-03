# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbifdb(RPackage):
	"""High Performance Interface to 'GBIF'

	A high performance interface to the Global Biodiversity
  Information Facility, 'GBIF'.  In contrast to 'rgbif', which can
  access small subsets of 'GBIF' data through web-based queries to
  a central server, 'gbifdb' provides enhanced performance for R users
  performing large-scale analyses on servers and cloud computing
  providers, providing full support for arbitrary 'SQL' or 'dplyr'
  operations on the complete 'GBIF' data tables (now over 1 billion
  records, and over a terabyte in size). 'gbifdb' accesses a copy
  of the 'GBIF' data in 'parquet' format, which is already readily
  available in commercial computing clouds such as the Amazon Open
  Data portal and the Microsoft Planetary Computer, or can be 
  accessed directly without downloading, or downloaded
  to any server with suitable bandwidth and storage space.
  The high-performance techniques for local and remote access 
  are described in <https://duckdb.org/why_duckdb>
  and <https://arrow.apache.org/docs/r/articles/fs.html> respectively.
	"""
	
	homepage = "https://docs.ropensci.org/gbifdb/"
	cran = "gbifdb" 

	version("1.0.0", md5="dafecbd86ab7928de9fa875e4a97910b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-arrow@8:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-duckdbfs", type=("build", "run"))
