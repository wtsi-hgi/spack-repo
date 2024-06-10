# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install pbminimap2
#
# You can edit this file again by typing:
#
#     spack edit pbminimap2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbminimap2(MesonPackage):
    """A fork of the minimap2 package from lh3/minimap2 used as PacBio packages dependency.

    Minimap2 is a versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database.
    Typical use cases include:
    (1) mapping PacBio or Oxford Nanopore genomic reads to the human genome;
    (2) finding overlaps between long reads with error rate up to ~15%;
    (3) splice-aware alignment of PacBio Iso-Seq or Nanopore cDNA or Direct RNA reads against a reference genome;
    (4) aligning Illumina single- or paired-end reads;
    (5) assembly-to-assembly alignment;
    (6) full-genome alignment between two closely related species with divergence below ~15%.
    """

    homepage = "https://github.com/PacificBiosciences/minimap2"
    git = "https://github.com/PacificBiosciences/minimap2.git"

    license("MIT")

    version("2.26", branch="2.26-meson")

    depends_on("zlib-api", type=("build", "run"))
