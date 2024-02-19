# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScallele(PythonPackage):
    """scAllele is a versatile tool to detect and analyze nucleotide variants in scRNA-seq."""

    homepage = "https://github.com/gxiaolab/scAllele"
    pypi = "scAllele/scAllele-0.0.9.3.tar.gz"

    version("0.0.9.3", sha256="fe0c3d8c1a4dadea52d04d64d319224edd87189195b2767b2ed9c441b16e3b3c")

    depends_on("python@3:3.8", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-glob2", type=("build", "run"))
    depends_on("py-htseq", type=("build", "run"))
    depends_on("py-multiprocess", type=("build", "run"))
    depends_on("py-networkx@2.4:", type=("build", "run"))
    depends_on("py-numpy@1.18.5:", type=("build", "run"))
    depends_on("py-pandas@1.3", type=("build", "run"))
    depends_on("py-pickleshare", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pyfaidx@0.5.9.5:", type=("build", "run"))
    depends_on("py-pysam@0.9.1:", type=("build", "run"))
    depends_on("py-vcfpy", type=("build", "run"))
    depends_on("py-scikit-learn@0.23.1:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-statsmodels@0.11.1:", type=("build", "run"))
