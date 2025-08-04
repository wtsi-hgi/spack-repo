# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Dnacomb(Package):
    """CLI tool for counting structured single and paired end sequencing reads and comparing them to an expected library. It compares each read to a canonical form defined in a library specification using one of four approaches:"""

    homepage = "https://github.com/allydunham/dnacomb"
    url = "https://github.com/allydunham/dnacomb/archive/refs/tags/v0.2.0.tar.gz"

    version("0.2.0", sha256="63e75e9f099c0975818b0327d0019761b60c73fe142ba68e437c7caa6a6eb526")
    version("0.1.0", sha256="25310c46ee0da65f05de7dfc97fabd5fbfbd2646c49477897a4487d530a9dc8f")
    
    depends_on("rust", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release")
        mkdirp(prefix.bin)
        install("target/release/dnacomb", prefix.bin)
