# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeg(RPackage):
	"""Chain Event Graph

	Create and learn Chain Event Graph (CEG) models using a Bayesian 
    framework. It provides us with a Hierarchical Agglomerative algorithm to 
    search the CEG model space.
    The package also includes several facilities for visualisations of the
    objects associated with a CEG. The CEG class can represent a range of
    relational data types, and supports arbitrary vertex, edge and graph
    attributes. A Chain Event Graph is a tree-based graphical model that
    provides a powerful graphical interface through which domain experts can
    easily translate a process into sequences of observed events using plain
    language. CEGs have been a useful class of graphical model especially to
    capture context-specific conditional independences. References: Collazo R, 
    Gorgen C, Smith J. Chain Event Graph. CRC Press, ISBN 9781498729604, 2018
    (forthcoming); and Barday LM, Collazo RA, Smith JQ, Thwaites PA, Nicholson AE. 
    The Dynamic Chain Event Graph. Electronic Journal of Statistics, 9 (2) 2130-2169
    <doi:10.1214/15-EJS1068>.
	"""
	
	homepage = "https://github.com/ptaranti/ceg"
	cran = "ceg" 

	version("0.1.0", md5="dc03185ab64429bdca6e6f06e6d04e93")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
