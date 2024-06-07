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
#     spack install pbipa
#
# You can edit this file again by typing:
#
#     spack edit pbipa
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import glob


class Pbipa(Package):
    """
    Improved Phased Assembler (IPA)🍺 is the official PacBio software for HiFi genome assembly.
    IPA was designed to utilize the accuracy of PacBio HiFi reads to produce high-quality phased genome assemblies.
    IPA is an end-to-end solution, starting with input reads and resulting in a polished assembly.
    IPA is fast, providing an easy to use local run mode or a distributed pipeline for a cluster.
    """

    homepage = "https://github.com/PacificBiosciences/pbipa"
    url = "https://github.com/PacificBiosciences/pbipa/releases/download/v1.8.0/pbipa.tar.gz"

    license("BSD-3-Clause-Clear license")

    version("1.8.0", sha256="8c08fc53a17dfc6e773c10a3e565ea7224595829e0b48adcd76556418544388a")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(self.stage.source_path + "/bin", prefix.bin)
        chmod = which("chmod")
        for executable in glob.glob(prefix.bin):
            chmod("+x", executable)
