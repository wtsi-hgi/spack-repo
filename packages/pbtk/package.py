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
#     spack install pbtk
#
# You can edit this file again by typing:
#
#     spack edit pbtk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import glob


class Pbtk(Package):
    """
    This repository is replacing individual tool repositories and binaries from pbbam.

    bam2fasta
    bam2fastq
    ccs-kinetics-bystrandify
    extracthifi
    pbindex
    pbindexdump
    pbmerge
    zmwfilter
    """

    homepage = "https://github.com/PacificBiosciences/pbtk"
    url = "https://github.com/PacificBiosciences/pbtk/releases/download/v3.1.1/pbtk.tar.gz"

    license("BSD-3-Clause-Clear license")

    version("3.1.1", sha256="4dbe08d880a4b54d7c84ecdf9849feead71ac5330277a66f57a2915447169814")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(self.stage.source_path, prefix.bin)
        chmod = which("chmod")
        for executable in glob.glob(prefix.bin):
            chmod("+x", executable)
