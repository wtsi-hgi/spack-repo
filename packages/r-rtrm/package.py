# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrm(RPackage):
    """Identification of Transcriptional Regulatory Modules from Protein-Protein Interaction Networks

    rTRM identifies transcriptional regulatory modules (TRMs) from protein-protein interaction networks.
    """

    homepage = "https://github.com/ddiez/rTRM"
    bioc = "rTRM"

    version("1.46.0", commit="f88021127c7db19d74aff244c8e26efe9ed9778f")
    version("1.40.0", commit="d1183dd8d57871ba3fee567730d1e7e977ebb4b2")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-igraph@1:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
