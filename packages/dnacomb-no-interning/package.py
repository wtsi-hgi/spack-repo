# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class DnacombNoInterning(Package):
    """CLI tool for flexibly parsing structured sequence reads into count tables and comparing them to expected libraries"""

    homepage = "https://github.com/allydunham/dnacomb"
    git = "https://github.com/allydunham/dnacomb.git"

    version("0.6.0rc1", commit="0807765c8a451e1f0f1291261e38067daca14ece")
    
    depends_on("rust", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release", "--no-default-features")
        mkdirp(prefix.bin)
        install("target/release/dnacomb", prefix.bin)
