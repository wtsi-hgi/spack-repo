# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemdist(RPackage):
	"""Information Accretion-based Function Predictor Evaluation

	This package implements methods to calculate information accretion for a given version of the gene ontology and uses this data to calculate remaining uncertainty, misinformation, and semantic similarity for given sets of predicted annotations and true annotations from a protein function predictor.
	"""
	
	homepage = "http://github.com/iangonzalez/SemDist"
	bioc = "SemDist" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SemDist_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SemDist/SemDist_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="3f86cfea1d6de9f097c4a764edf40923a820ba2dd57a8bd17a32c31192711f98")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
