# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreg(RPackage):
    """Tools for finding Total RNA Expression Genes in single nucleus RNA-seq data

    RNA abundance and cell size parameters could improve RNA-seq deconvolution algorithms to more accurately estimate cell type proportions given the different cell type transcription activity levels. A Total RNA Expression Gene (TREG) can facilitate estimating total RNA content using single molecule fluorescent in situ hybridization (smFISH). We developed a data-driven approach using a measure of expression invariance to find candidate TREGs in postmortem human brain single nucleus RNA-seq. This R package implements the method for identifying candidate TREGs from snRNA-seq data.
    """

    homepage = "https://github.com/LieberInstitute/TREG"
    bioc = "TREG"

    version("1.12.0", commit="cd017799ee7b937fa6d15141f0a26bb0162852ec")
    version("1.6.0", commit="fcf0640b15a5306f59c2899bac852e4c8f371c7d")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rafalib", type=("build", "run"))
