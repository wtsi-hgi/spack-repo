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

	version("1.42.0", commit="2ae4e5b5aa56575be531024ea272189c7623a56f")
	version("1.36.0", commit="a1df6d9ad15e41a24dc8717a9d89ef69f755a551")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gviz@1.7.10:", type=("build", "run"))
	depends_on("r-biovizbase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
