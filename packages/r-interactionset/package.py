# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractionset(RPackage):
	"""Base Classes for Storing Genomic Interaction Data

	Provides the GInteractions, InteractionSet and ContactMatrix objects and associated methods for storing and manipulating genomic interaction data from Hi-C and ChIA-PET experiments.
	"""
	
	bioc = "InteractionSet"

	version("1.36.1", commit="5e17b72b4efb65a180acc04b8d87355715f9053f")
	version("1.30.0", commit="43e670bada510d5d329c990ce86c6ce3621c9b91")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.27.12:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
