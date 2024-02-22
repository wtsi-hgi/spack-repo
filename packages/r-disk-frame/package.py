# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiskFrame(RPackage):
	"""Larger-than-RAM Disk-Based Data Manipulation Framework

	A disk-based data manipulation tool for working with 
  large-than-RAM datasets. Aims to lower the barrier-to-entry for 
  manipulating large datasets by adhering closely to popular and 
  familiar data manipulation paradigms like 'dplyr' verbs and 
  'data.table' syntax.
	"""
	
	homepage = "https://diskframe.com"
	cran = "disk.frame" 

	version("0.8.3", md5="825de93939e4a3f82b22a4f0bd5bba6f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-future-apply@1.3:", type=("build", "run"))
	depends_on("r-fs@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-pryr@0.1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-fst@0.8:", type=("build", "run"))
	depends_on("r-future@1.14:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-bigreadr@0.2:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-benchmarkme", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-globals", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
