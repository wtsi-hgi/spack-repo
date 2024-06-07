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
#     spack install pbskera
#
# You can edit this file again by typing:
#
#     spack edit pbskera
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbskera(Package):
    """
    Skera splits MAS-Seq PacBio HiFi reads at adapter positions generating segmented reads (S-reads).
    For each input/parent read (e.g. HiFi) skera will create multiple bam records, one for each S-read.
    A parent read can contain many S-reads. Skera has two major functions, split and undo.
    Skera undo reconstitutes the original parent read from input S-reads.
    """

    homepage = "http://skera.how"
    url = "https://github.com/PacificBiosciences/skera/releases/download/v1.2.0/skera"

    license(" BSD-3-Clause-Clear license")

    version("1.2.0", sha256="0385ab4d67377cd6ed596eccd5df973c03d78561db639d84f9ff557332f745be", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/skera", prefix.bin.pbskera)
        chmod = which("chmod")
        chmod("+x", prefix.bin.pbskera)
