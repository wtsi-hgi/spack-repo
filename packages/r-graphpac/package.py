# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphpac(RPackage):
	"""Identification of Mutational Clusters in Proteins via a Graph Theoretical Approach.

	Identifies mutational clusters of amino acids in a protein while utilizing the proteins tertiary structure via a graph theoretical model.
	"""
	
	bioc = "GraphPAC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GraphPAC_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GraphPAC/GraphPAC_1.44.0.tar.gz"]

	version("1.44.0", sha256="aa6c81bcb15b6d34115783fb8e00cad4e6b1247724789135455cda82fc46e8b7")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ipac", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-rmallow", type=("build", "run"))
