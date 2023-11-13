# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDemultiplex(PythonPackage):
    """Demultiplex any number of FASTA or a FASTQ files based on a list of barcodes"""

    homepage = "https://pypi.org/project/demultiplex/"
    pypi = "demultiplex/demultiplex-1.2.2.tar.gz"

    version("1.2.2", sha256="27ebc30e52e36048486286348b44806deabb24197e05eb88bbed413676e99181")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-biopython@1.73", type=("build", "run"))
    depends_on("py-python-levenshtein", type=("build", "run"))
    depends_on("py-regex", type=("build", "run"))

    depends_on("py-tssv@1.1.0", type=("build", "run"))
    depends_on("py-jit-open@1.0.1", type=("build", "run"))
    depends_on("py-fastools@1.1.0", type=("build", "run"))
    depends_on("py-dict-trie@1.0.1", type=("build", "run"))

