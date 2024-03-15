# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeiden(RPackage):
	"""R Implementation of Leiden Clustering Algorithm.

	Implements the 'Python leidenalg' module to be called in R. Enables
	clustering using the leiden algorithm for partition a graph into
	communities. See the 'Python' repository for more details:
	<https://github.com/vtraag/leidenalg> Traag et al (2018) From Louvain to
	Leiden: guaranteeing well-connected communities. <arXiv:1810.08473>."""

	cran = "leiden"

	license("GPL-3.0-only OR custom")

	version("0.4.3.1", md5="8afbadc336cd24e8d6f52fad7ca5b6ae")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph@1.2.7:", type=("build", "run"))
