# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROscope(RPackage):
    """Oscope - A statistical pipeline for identifying oscillatory genes in unsynchronized single cell RNA-seq

    Oscope is a statistical pipeline developed to identifying and recovering the base cycle profiles of oscillating genes in an unsynchronized single cell RNA-seq experiment. The Oscope pipeline includes three modules: a sine model module to search for candidate oscillator pairs; a K-medoids clustering module to cluster candidate oscillators into groups; and an extended nearest insertion module to recover the base cycle order for each oscillator group.
    """

    bioc = "Oscope"

    version("1.38.0", commit="ed0be791275937107d08d9af77d6432bc42f9a3f")
    version("1.32.0", commit="44ec9233170da151bff7cb911a863557b8c14f16")

    depends_on("r-ebseq", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
