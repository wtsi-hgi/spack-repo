# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBionet(RPackage):
    """Routines for the functional analysis of biological networks

    This package provides functions for the integrated analysis of protein-protein interaction networks and the detection of functional modules. Different datasets can be integrated into the network by assigning p-values of statistical tests to the nodes of the network. E.g. p-values obtained from the differential expression of the genes from an Affymetrix array are assigned to the nodes of the network. By fitting a beta-uniform mixture model and calculating scores from the p-values, overall scores of network regions can be calculated and an integer linear programming algorithm identifies the maximum scoring subnetwork.
    """

    homepage = "http://bionet.bioapps.biozentrum.uni-wuerzburg.de/"
    bioc = "BioNet"

    version("1.68.0", commit="72d088120c9b76be0b5907b3a1174e7ee71a361b")
    version("1.62.0", commit="760e83de5d9df18e899f4f2a24f6ded39d63e6ba")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-igraph@1.0.1:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
