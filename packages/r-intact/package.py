# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntact(RPackage):
    """Integrate TWAS and Colocalization Analysis for Gene Set Enrichment Analysis

    This package integrates colocalization probabilities from colocalization analysis with transcriptome-wide association study (TWAS) scan summary statistics to implicate genes that may be biologically relevant to a complex trait. The probabilistic framework implemented in this package constrains the TWAS scan z-score-based likelihood using a gene-level colocalization probability. Given gene set annotations, this package can estimate gene set enrichment using posterior probabilities from the TWAS-colocalization integration step.
    """

    homepage = "https://github.com/jokamoto97/INTACT"
    bioc = "INTACT"

    version("1.8.0", commit="4b6725cdb637624cf5b88220f9278abb8bcf142f")
    version("1.2.0", commit="0b5c6690850ddf7567098e081f00d238c5cc90c7")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-squarem", type=("build", "run"))
    depends_on("r-bdsmatrix", type=("build", "run"))
    depends_on("r-numderiv", type=("build", "run"))
