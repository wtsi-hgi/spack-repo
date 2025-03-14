# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmultiome(RPackage):
    """Collection of Public Single-Cell Multiome (scATAC + scRNAseq) Datasets

    Single cell multiome data, containing chromatin accessibility (scATAC-seq) and gene expression (scRNA-seq) information analyzed with the ArchR package and presented as MultiAssayExperiment objects.
    """

    bioc = "scMultiome"
    url = "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/scMultiome_1.6.0.tar.gz"

    version("1.6.0", sha256="be0c4fbb7e37a5f29be19b753e3288eb8b36d319cb200b854efeaa807799d2f1")

    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-experimenthub@2.8.1:", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-azurestor", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-alabaster-matrix", type=("build", "run"))

