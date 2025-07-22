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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/QuartPAC_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/QuartPAC/QuartPAC_1.34.0.tar.gz"]

	version("1.34.0", sha256="c4f882efe5099b332ddb35308bc729a4265f88b0aa53380102223f2bc1084e21")

	depends_on("r-ipac", type=("build", "run"))
	depends_on("r-graphpac", type=("build", "run"))
	depends_on("r-spacepac", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
