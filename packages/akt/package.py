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
#     spack install akt
#
# You can edit this file again by typing:
#
#     spack edit akt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Akt(MakefilePackage):
    """Ancestry and Kinship Tools (AKT) provides a handful of useful statistical genetics routines using the htslib API for input/output. This means it can seamlessly read BCF/VCF files and play nicely with bcftools."""

    homepage = "https://github.com/Illumina/akt"
    url = "https://github.com/Illumina/akt/archive/refs/tags/v0.3.3.tar.gz"

    license("GPL-3.0")

    version("0.3.3", sha256="1b077dde944cb13132e4fb5b47d4930c1ecfc74b299c95fe3cc7bf5c17b8f710")

    depends_on("zlib-api")

    def patch(self):
        which("chmod")("+x", "htslib-1.6/version.sh")
        filter_file("$(shell git describe --abbrev=4 --always )", "v{}".format(self.version), "Makefile", string=True)
        filter_file("#define BGZF_MAX_BLOCK_SIZE 0x10000", "#define BGZF_MAX_BLOCK_SIZE 74000", "htslib-1.6/htslib/bgzf.h", string=True) # https://github.com/samtools/htslib/issues/1257#issuecomment-804769847
        
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("akt", prefix.bin)
