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
#     spack install pbfusion
#
# You can edit this file again by typing:
#
#     spack edit pbfusion
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbfusion(Package):
    """PacBio Fusion Detection - pbfusion.

    Eukaryotic RNA processing complexity introduces a number of modes for transcriptional abnormalities
    which are not true fusion events. These include trans splicing, read-through events, and sense-antisense
    chimeras. Additionally, due to overlapping genes/exons, annotating the precise gene combinations
    correctly cannot always be solved.

    To handle this, we classify fusions by quality (LOW, MEDIUM, and HIGH) as well as by event type.
    """

    homepage = "https://github.com/PacificBiosciences/pbfusion"
    url = "https://github.com/PacificBiosciences/pbfusion/releases/download/0.4.1/pbfusion-v0.4.1-linux_x86_64.gz"

    license("BSD-3-Clause-Clear license")

    version("0.4.1", sha256="c6abde2ee1f88355158bf1c655e5ae754f942708f7addbaef8d626fdebfcfe7a")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/pbfusion-v0.4.1-linux_x86_64", prefix.bin.pbfusion)
        chmod = which("chmod")
        chmod("+x", prefix.bin.pbfusion)
