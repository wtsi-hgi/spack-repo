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
#     spack install pbsv
#
# You can edit this file again by typing:
#
#     spack edit pbsv
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbsv(Package):
    """
    pbsv is a suite of tools to call and analyze structural variants in diploid genomes from
    PacBio single molecule real-time sequencing (SMRT) reads. The tools power the Structural
    Variant Calling analysis workflow in PacBio's SMRT Link GUI.
    """

    homepage = "https://github.com/PacificBiosciences/pbsv"
    url = "https://github.com/PacificBiosciences/pbsv/releases/download/v2.9.0/pbsv"

    license("BSD-3-Clause-Clear")

    version("2.9.0", sha256="3daf41d28f5d0063f68c49ce790ab17b648f1d2459122f5c13704598342db97c", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/pbsv", prefix.bin.pbsv)
        chmod = which("chmod")
        chmod("+x", prefix.bin.pbsv)
