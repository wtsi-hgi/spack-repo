# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliquems(RPackage):
	"""Annotation of Isotopes, Adducts and Fragmentation Adducts for in-Source LC/MS Metabolomics Data

	Annotates data from liquid chromatography coupled to mass spectrometry (LC/MS) metabolomics experiments. Based on a network algorithm (O.Senan, A. Aguilar- Mogas, M. Navarro, O. Yanes, R.Guimerà and M. Sales-Pardo, Bioinformatics, 35(20), 2019), 'CliqueMS' builds a weighted similarity network where nodes are features and edges are weighted according to the similarity of this features. Then it searches for the most plausible division of the similarity network into cliques (fully connected components). Finally it annotates metabolites within each clique, obtaining for each annotated metabolite the neutral mass and their features, corresponding to isotopes, ionization adducts and fragmentation adducts of that metabolite.
	"""
	
	homepage = "http://cliquems.seeslab.net"
	bioc = "cliqueMS"

	version("1.22.0", commit="c7c28736b9f8d51e37b6cb19ced9989506897a33")
	version("1.16.0", commit="18f44830ad8d3dbdaf19228351a6caa710205b43")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xcms@3:", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-qlcmatrix", type=("build", "link", "run"))
