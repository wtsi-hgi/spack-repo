# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class EnsemblVep(Package):
    """VEP (Variant Effect Predictor) predicts the functional effects of genomic variants."""

    homepage = "https://www.ensembl.org/vep"
    git = "https://github.com/Ensembl/ensembl-vep"

    version("110.1", tag="release/110.1")
    version("110.0", tag="release/110.0")
    version("109.3", tag="release/109.3")
    version("109.2", tag="release/109.2")
    version("109.1", tag="release/109.1")
    version("109.0", tag="release/109.0")
    version("108.2", tag="release/108.2")
    version("108.1", tag="release/108.1")
    version("108.0", tag="release/108.0")
    version("107.0", tag="release/107.0")

    depends_on("perl")
    depends_on("perl-dbi")
    depends_on("perl-archive-zip")
    depends_on("perl-dbd-mysql")
    depends_on("perl-set-intervaltree")
    depends_on("perl-json")
    depends_on("perl-perlio-gzip")
    depends_on("perl-bio-bigfile")
    depends_on("perl-clone")
    depends_on("bzip2", type="build")
    depends_on("xz", type="build")
    depends_on("lzma", type="build")

    patch("deps.patch")

    def install(self, spec, prefix):
        perl = which("perl")
        perl("INSTALL.pl", "--NO_TEST", "--AUTO", "al")
        install_tree(".", join_path(self.prefix, "usr", "local", "share", "vep"))
