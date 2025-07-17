# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeggorthology(RPackage):
    """graph support for KO, KEGG Orthology

    graphical representation of the Feb 2010 KEGG Orthology. The KEGG orthology is a set of pathway IDs that are not to be confused with the KEGG ortholog IDs.
    """

    bioc = "keggorthology"

    version("2.60.0", commit="550c8bd8272bb385958bc3ff9d018b772fb7e4b4")
    version("2.54.0", commit="86332c3747bcc4b724ddf88bf9979fdc02b599c3")

    depends_on("r@2.5:", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-hgu95av2-db", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
