# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkcomm(RPackage):
	"""Tools for Generating, Visualizing, and Analysing Link
Communities in Networks

	Link communities reveal the nested and overlapping
    structure in networks, and uncover the key nodes that form connections
    to multiple communities. linkcomm provides a set of tools for
    generating, visualizing, and analysing link communities in networks of
    arbitrary size and type. The linkcomm package also includes tools for
    generating, visualizing, and analysing Overlapping Cluster Generator
    (OCG) communities. Kalinka and Tomancak (2011) <doi:10.1093/bioinformatics/btr311>.
	"""
	
	homepage = "https://alextkalinka.github.io/linkcomm/"
	cran = "linkcomm" 

	version("1.0-14", md5="57d4704b221da3a45be71a7466827c89")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
