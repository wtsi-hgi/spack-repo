# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeberdivechalcdata(RPackage):
    """Spatially-resolved transcriptomics and single-nucleus RNA-sequencing data from the locus coeruleus (LC) in postmortem human brain samples

    Spatially-resolved transcriptomics (SRT) and single-nucleus RNA-sequencing (snRNA-seq) data from the locus coeruleus (LC) in postmortem human brain samples. Data were generated with the 10x Genomics Visium SRT and 10x Genomics Chromium snRNA-seq platforms. Datasets are stored in SpatialExperiment and SingleCellExperiment formats.
    """

    homepage = "https://github.com/lmweber/WeberDivechaLCdata"
    bioc = "WeberDivechaLCdata"

    version("1.10.0", commit="8133353967ea7b2bcfd996fe367c392ade76141c")
    version("1.4.1", commit="45c40fdcdc6aa99df5338296d12f89cd3bc48a59")
    version("1.4.0", md5="3b75c693f86ed228e2b7816872cfe4b7")

    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
