# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighlyreplicatedrnaseq(RPackage):
    """Collection of Bulk RNA-Seq Experiments With Many Replicates

    Gene-level count matrix data for bulk RNA-seq dataset with many replicates. The data are provided as easy to use SummarizedExperiment objects. The source data that is made accessible through this package comes from https://github.com/bartongroup/profDGE48.
    """

    homepage = "https://github.com/const-ae/HighlyReplicatedRNASeq"
    bioc = "HighlyReplicatedRNASeq"

    version("1.20.0", commit="03054fcb3b7201a8d499afc75e9449ac98d89f30")
    version("1.14.0", commit="1dd0c87e96b47f7e660ce6f45f04eeb147f4b249")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
