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
#     spack install recalladapters
#
# You can edit this file again by typing:
#
#     spack edit recalladapters
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Recalladapters(Package):
    """A tool to recall adapters for PacBio data.

    recalladapters provides a way to change the adapter calls in a PacBio BAM file.
    It accepts a subreads.bam and a scraps.bam, and emits a subreads.bam and scraps.bam.
    Basecalls may be moved between files (e.g. as new adapters are found and moved to scraps),
    and BAM records may be split or concatenated (e.g. two subreads will be concatenated if the
    adapter between them is ignored).

    See our File Format Primer for more information on the relationship between PacBio SMRTBells,
    subreads and adapters: https://pacbiofileformats.readthedocs.io/en/5.1/Primer.html

    This tool allows users to modify the adapter sequences used in adapter finding, for instance
    if an incorrect set of adapters was specified on-instrument. It can also be used to modify
    adapter finding parameters, for instance to increase the importance of the flank alignment
    when filtering out false positive adapter calls.
    """

    homepage = "https://github.com/PacificBiosciences/recalladapters"
    url = "https://github.com/PacificBiosciences/recalladapters/releases/download/v9.0.0/recalladapters"

    license("BSD-3-Clause-Clear license")

    version("9.0.0", sha256="409877fc15746e8c1f68b8ee09fb9050c849c73d3a3b8c4a73ca34a21e3c719c", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/recalladapters", prefix.bin.recalladapters)
        chmod = which("chmod")
        chmod("+x", prefix.bin.recalladapters)
