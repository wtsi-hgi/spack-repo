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
#     spack install isoseq
#
# You can edit this file again by typing:
#
#     spack edit isoseq
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Isoseq(Package):
    """
    IsoSeq contains the newest tools to identify transcripts
    in PacBio single-molecule sequencing data.
    """

    homepage = "https://github.com/PacificBiosciences/IsoSeq"
    url = "https://github.com/PacificBiosciences/IsoSeq/releases/download/v4.0.0/isoseq"

    license("BSD-3-Clause-Clear")

    version(
        "4.0.0",
        sha256="5766001507cf2a351b260cf38b717351dd676a7c87eb7c285c3c43a4a458f4b2",
        expand=False,
    )

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/isoseq", prefix.bin.isoseq)
        chmod = which("chmod")
        chmod("+x", prefix.bin.isoseq)
