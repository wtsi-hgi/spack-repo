# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssessorf(RPackage):
    """Assess Gene Predictions Using Proteomics and Evolutionary Conservation

    In order to assess the quality of a set of predicted genes for a genome, evidence must first be mapped to that genome. Next, each gene must be categorized based on how strong the evidence is for or against that gene. The AssessORF package provides the functions and class structures necessary for accomplishing those tasks, using proteomic hits and evolutionarily conserved start codons as the forms of evidence.
    """

    bioc = "AssessORF"

    version("1.26.0", commit="8ed0e3392356e42817a88c9952963ad4f1b1fce0")
    version("1.20.0", commit="70f63631742811437624c798a7efa08a31420ebd")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-decipher@2.10:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
