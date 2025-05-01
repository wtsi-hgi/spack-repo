# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Isoseq(Package):
    """
    IsoSeq contains the newest tools to identify transcripts
    in PacBio single-molecule sequencing data.
    """

    homepage = "https://isoseq.how"
    url = "https://github.com/PacificBiosciences/IsoSeq/releases/download/v4.0.0/isoseq"

    license("BSD-3-Clause-Clear")

    version("4.3.0", sha256="7af9b3001a9717e730e9c7858b0a7ef3e9af47b7420539371b886fd7b67c29d5", expand=False)
    version("4.0.0", sha256="5766001507cf2a351b260cf38b717351dd676a7c87eb7c285c3c43a4a458f4b2", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/isoseq", prefix.bin.isoseq)
        chmod = which("chmod")
        chmod("+x", prefix.bin.isoseq)
