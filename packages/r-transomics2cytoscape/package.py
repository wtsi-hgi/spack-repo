# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransomics2cytoscape(RPackage):
    """A tool set for 3D Trans-Omic network visualization with Cytoscape

    transomics2cytoscape generates a file for 3D transomics visualization by providing input that specifies the IDs of multiple KEGG pathway layers, their corresponding Z-axis heights, and an input that represents the edges between the pathway layers. The edges are used, for example, to describe the relationships between kinase on a pathway and enzyme on another pathway. This package automates creation of a transomics network as shown in the figure in Yugi.2014 (https://doi.org/10.1016/j.celrep.2014.07.021) using Cytoscape automation (https://doi.org/10.1186/s13059-019-1758-4).
    """

    bioc = "transomics2cytoscape"

    version("1.18.0", commit="1756878f4a5281605b287c22f80776654731b3e7")
    version("1.12.0", commit="29a2d4e74806cd5bbcc5e124335188873183a4cd")

    depends_on("r-rcy3", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("cytoscape@3.10.0:", type=("build", "link", "run"))
