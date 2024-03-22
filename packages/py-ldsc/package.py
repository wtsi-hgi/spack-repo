# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyLdsc(PythonPackage):
    """ldsc is a command line tool for estimating heritability and genetic correlation from GWAS summary statistics. ldsc also computes LD Scores."""

    homepage = "https://github.com/belowlab/ldsc/tree/2-to-3"
    git = "https://github.com/belowlab/ldsc/tree/2-to-3"
    pypi = "ldsc/ldsc-2.0.1.tar.gz"

    version("2.0.1", sha256="fe72f99da8a26414d82e47f2d2ee7cebbbab6c20d1b4ea51a0c38cc650c63556")

    depends_on("python@3.9.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-bitarray@2.6.0", type=("build", "run"))
    depends_on("py-nose@1.3.7", type=("build", "run"))
    depends_on("py-pybedtools@0.9.0", type=("build", "run"))
    depends_on("py-scipy@1.9.2", type=("build", "run"))
    depends_on("py-pandas@1.5.0", type=("build", "run"))
    depends_on("py-numpy@1.23.3", type=("build", "run"))
