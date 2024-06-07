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
#     spack install pbccs
#
# You can edit this file again by typing:
#
#     spack edit pbccs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbccs(Package):
    """
    ccs combines multiple subreads of the same SMRTbell molecule using a statistical model to produce one
    highly accurate consensus sequence, also called a HiFi read, along with base quality values. This tool
    powers the Circular Consensus Sequencing workflow in SMRT Link for Sequel and Sequel II platform.
    On Sequel IIe and Revio platforms, HiFi generation is perfomed on the instrument.
    """

    homepage = "https://ccs.how/"
    url = "https://github.com/PacificBiosciences/ccs/releases/download/v6.4.0/ccs.tar.gz"

    license("BSD-3-Clause-Clear license")

    version("6.4.0", sha256="7aac013844b45c727139aed5f18d2d7f44293ab6446b0f53199b1313a98e9ad2")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/ccs", prefix.bin.ccs)
        install(self.stage.source_path + "/ccs-alt", join_path(prefix.bin, "ccs-alt"))
        chmod = which("chmod")
        chmod("+x", prefix.bin.ccs)
        chmod("+x", join_path(prefix.bin, "ccs-alt"))
