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
#     spack install pbmarkdup
#
# You can edit this file again by typing:
#
#     spack edit pbmarkdup
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbmarkdup(Package):
    """Mark duplicate reads from PacBio sequencing of an amplified library.

    pbmarkdup takes one or multiple sequencing chips of an amplified libray
    as HiFi reads and marks or removes duplicates.
    """

    homepage = "https://github.com/PacificBiosciences/pbmarkdup"
    url = "https://github.com/PacificBiosciences/pbmarkdup/releases/download/v1.0.3/pbmarkdup"

    license("BSD-3-Clause-Clear license")

    version("1.0.3", sha256="96907ba4873f377c79b3c74128ae45307e75e7c42dd90b0ddf7fe8b4684b723a", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/pbmarkdup", prefix.bin.pbmarkdup)
        chmod = which("chmod")
        chmod("+x", prefix.bin.pbmarkdup)
