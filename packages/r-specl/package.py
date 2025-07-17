# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecl(RPackage):
    """specL - Prepare Peptide Spectrum Matches for Use in Targeted Proteomics

    provides a functions for generating spectra libraries that can be used for MRM SRM MS workflows in proteomics. The package provides a BiblioSpec reader, a function which can add the protein information using a FASTA formatted amino acid file, and an export method for using the created library in the Spectronaut software. The package is developed, tested and used at the Functional Genomics Center Zurich <https://fgcz.ch>.
    """

    homepage = "http://bioconductor.org/packages/specL/"
    bioc = "specL"

    version("1.42.0", commit="803d372d9587ab07f1b0ce4303a6b552e4daf325")
    version("1.36.0", commit="10a96640df01e063f46eac3d462377e20f5f6706")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-dbi@0.5:", type=("build", "run"))
    depends_on("r-protviz@0.7:", type=("build", "run"))
    depends_on("r-rsqlite@1.1:", type=("build", "run"))
    depends_on("r-seqinr@3.3:", type=("build", "run"))
