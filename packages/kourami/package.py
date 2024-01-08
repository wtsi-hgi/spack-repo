# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class Kourami(MavenPackage):
    """Kourami is a graph-guided assembler for HLA haplotypes covering typing exons (exons 2 and 3 for Class I and exon 3 for Class II) using high-coverage whole genome sequencing data."""

    homepage = "https://github.com/Kingsford-Group/Kourami"
    url = "https://github.com/Kingsford-Group/kourami/archive/refs/tags/v0.9.6.tar.gz"

    version("0.9.6", sha256="e2f9ddf0d67f5f233e52cfd9fa9c3c15b534c5249aba68c6df2bbddc3c401098")
    version("0.9.5", sha256="c6019ccdc1e73c43cebabfb4e9f8e06f69f4f3afd22adccd2d8a371435639d6a")
    version("0.9.4", sha256="19060169294c901ec0ab268ea34af2e74709048b80c00d7845895764503dd490")
    version("0.9.2", sha256="534ab8b0dcc269c10c220481c4f9914ccacbfbf0bb64cdd51bd77f5027692bda")
    version("0.9.1", sha256="867099aaab255fa14797b9fe96760caa4156e4aa7ea99486c9c4457f1b10eb49")
    version("0.9", sha256="727eca6f37d01c2c8119318cb0a30b3aeac75a2737b8ce8bd527f994f70aa0b1")

    def patch(self):
        mkdir("bin")
        with open("bin/kourami", "w") as fh:
            fh.write("#!/bin/bash\njava -jar " + self.prefix.target.Kourami +".jar")
        os.chmod("bin/kourami", 0o755)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)

