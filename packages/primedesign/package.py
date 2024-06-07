# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from os import chmod

class Primedesign(Package):
    """PrimeDesign is a software tool for the flexible and comprehensive design of prime editing. PrimeDesign is an edit-centric design tool for the installation of substitution, insertion, and deletion edits, and is generalizable for both single and combinatorial edits. Taking a single input that encodes both the reference and edit sequence, PrimeDesign enumerates all possible pegRNA protospacers, pegRNA extensions, and ngRNAs within set parameter ranges to install the desired edit(s).."""

    homepage = "https://drugthatgene.pinellolab.partners.org/"
    url = "https://github.com/pinellolab/PrimeDesign/archive/refs/tags/0.2.tar.gz"

    version("0.2", sha256="63e23717df7769612df0a8ab18f3bec87fe9193da75af0f4f2d5279a489f0c57")

    depends_on("python", type="run")

    def install(self, spec, prefix):
        file = "PrimeDesign/command_line/primedesign.py"
        filter_file("# Design pegRNAs and ngRNAs for prime editing", "#!"+spec["python"].prefix.bin.python+"\n# Design pegRNAs and ngRNAs for prime editing", file, string=True)
        mkdir(prefix.bin)
        chmod(file, 0o755)
        install(file, prefix.bin)
