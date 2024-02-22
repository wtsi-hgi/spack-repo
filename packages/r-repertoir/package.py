# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepertoir(RPackage):
	"""Repertoire Graphical Visualization

	Visualization platform for T cell receptor repertoire
    analysis output results. It includes comparison of sequence frequency
    among samples, network of similar sequences and convergent
    recombination source between species. Currently repertoire analysis is
    in early stage of development and requires new approaches for
    repertoire data examination and assessment as we intend to develop.
    No publication is available yet (will be available in the near
    future), Efroni (2021) <https:>.
	"""
	
	homepage = "https://github.com/systemsbiomed/RepertoiR"
	cran = "RepertoiR" 

	version("0.0.1", md5="24b099d3dc680022cb0401116b635255")

	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
