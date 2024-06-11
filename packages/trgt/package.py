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
#     spack install trgt
#
# You can edit this file again by typing:
#
#     spack edit trgt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Trgt(Package):
    """Tandem repeat genotyping tool for HiFi sequencing data.

    TRGT is a tool for targeted genotyping of tandem repeats from PacBio HiFi data. In addition to the basic
    size genotyping, TRGT profiles sequence composition, mosaicism, and CpG methylation of each analyzed
    repeat and visualization of reads overlapping the repeats.
    """

    homepage = "https://github.com/PacificBiosciences/trgt"
    url = "https://github.com/PacificBiosciences/trgt/archive/refs/tags/v1.0.0.tar.gz"

    license("Pacific Biosciences Software License")

    version("1.0.0", sha256="3e36014d5e448fbfde9e45b2971b6dc01ac889c6d409cb20a8f7a05d26bb3b3c")

    depends_on("rust@1.74:", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release")
        mkdirp(prefix.bin)
        install("target/release/trgt", prefix.bin)
