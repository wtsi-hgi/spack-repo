# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuartpac(RPackage):
	"""Identification of mutational clusters in protein quaternary structures.

	Identifies clustering of somatic mutations in proteins over the entire quaternary structure.
	"""
	
	bioc = "QuartPAC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/QuartPAC_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/QuartPAC/QuartPAC_1.34.0.tar.gz"]

	version("1.34.0", md5="91af5166d133016b9beaa8539f0fcef7")

	depends_on("r-ipac", type=("build", "run"))
	depends_on("r-graphpac", type=("build", "run"))
	depends_on("r-spacepac", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
