# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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

    license("BSD-3-Clause-Clear license")

    version("1.4.0", sha256="52ec9c9dbe58aaf4d37eee5147f70c2271f2426b12ade97d8c1c38d11e4b0574", expand=False)
    version("1.2.0", sha256="0385ab4d67377cd6ed596eccd5df973c03d78561db639d84f9ff557332f745be", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/skera", prefix.bin.pbskera)
        chmod = which("chmod")
        chmod("+x", prefix.bin.pbskera)
