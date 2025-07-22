# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaxtoolsr(RPackage):
    """Access Pathways from Multiple Databases Through BioPAX and Pathway Commons

    The package provides a set of R functions for interacting with BioPAX OWL files using Paxtools and the querying Pathway Commons (PC) molecular interaction database. Pathway Commons is a project by the Memorial Sloan-Kettering Cancer Center (MSKCC), Dana-Farber Cancer Institute (DFCI), and the University of Toronto. Pathway Commons databases include: BIND, BioGRID, CORUM, CTD, DIP, DrugBank, HPRD, HumanCyc, IntAct, KEGG, MirTarBase, Panther, PhosphoSitePlus, Reactome, RECON, TRANSFAC.
    """

    homepage = "https://github.com/BioPAX/paxtoolsr"
    bioc = "paxtoolsr"

    version("1.42.0", commit="ad23f4be5d89462559d72115af4acb901f718271")
    version("1.36.0", commit="efd04f22df892b622765187c508d3712fdd40670")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-rjava@0.9.8:", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
    depends_on("openjdk@1.6:", type=("build", "link", "run"))
