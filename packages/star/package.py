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
#     spack install star
#
# You can edit this file again by typing:
#
#     spack edit star
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Star(MakefilePackage):
    """Spliced Transcripts Alignment to a Reference © Alexander Dobin, 2009-2024 https://www.ncbi.nlm.nih.gov/pubmed/23104886."""

    homepage = "https://github.com/alexdobin/STAR"
    url = "https://github.com/alexdobin/STAR/archive/2.7.11b.tar.gz"

    license("MIT")

    version("2.7.11b", sha256="3f65305e4112bd154c7e22b333dcdaafc681f4a895048fa30fa7ae56cac408e7")
    version("2.7.11a", sha256="542457b1a4fee73f27a581b1776e9f73ad2b4d7e790388b6dc71147bd039f99a")
    version("2.7.10b", sha256="0d1b71de6c5be1c5d90b32130d2abcd5785a4fc7c1e9bf19cc391947f2dc46e5")

    depends_on("zlib-api")
    depends_on("xxd-standalone")

    build_directory = "source"

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("source/STAR", prefix.bin.STAR)
