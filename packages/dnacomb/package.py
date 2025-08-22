# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Dnacomb(Package):
    """CLI tool for counting structured single and paired end sequencing reads and comparing them to an expected library. It compares each read to a canonical form defined in a library specification using one of four approaches:"""

    homepage = "https://github.com/allydunham/dnacomb"
    git = "https://github.com/allydunham/dnacomb.git"

    version("0.2.2", commit="ac90aa97b3e7492612675fba9851fb489b5468c1")
    version("0.2.1", commit="bea1a3b19ede4bf6d5e45d38febd57721b329c91")
    version("0.2.0", commit="6c6b08fbd143867ffc270509988c747137d718b2")
    version("0.1.0", commit="77440a15ff50c021adc1899ae6b9a33288abd31d")
    
    depends_on("rust", type="build")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release")
        mkdirp(prefix.bin)
        install("target/release/dnacomb", prefix.bin)
