# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPviz(RPackage):
	"""Peptide Annotation and Data Visualization using Gviz

	Pviz adapts the Gviz package for protein sequences and data.
	"""
	
	bioc = "Pviz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Pviz_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Pviz/Pviz_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="8aa64a7d7253553b2d66c8754f62c51b0e3005553a9c7384f2b70ac4bc7e4f9d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gviz@1.7.10:", type=("build", "run"))
	depends_on("r-biovizbase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
