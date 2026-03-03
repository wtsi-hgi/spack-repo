# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhype(RPackage):
	"""Work with Hypergraphs in R

	Create and manipulate hypergraph objects. This early version of
    rhype allows for the output of matrices associated with the hypergraphs 
    themselves. It also uses these matrices to calculate hypergraph spectra and
    perform spectral comparison. Functionality coming soon includes calculation
    of hyperpaths and hypergraph centrality measures.
	"""
	
	cran = "rhype" 

	version("0.3.0", md5="2400467431e96f2f9cc3243c3c0435c0")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
