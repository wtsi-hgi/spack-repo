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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/InteractionSet_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/InteractionSet/InteractionSet_1.30.0.tar.gz"]

    version("1.36.1", tag="RELEASE_3_21")
	version("1.30.0", sha256="1a372f3d5e9908caf13ceaf67ca7cc9e80b3ecec23c965acbf649c0539ebef56")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.27.12:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
