# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGwaslab(PythonPackage):
    """A collection of handy tools for GWAS SumStats."""

    homepage = "https://cloufield.github.io/gwaslab/"
    pypi = "gwaslab/gwaslab-3.6.13.tar.gz"

    version("3.6.13", sha256="82ba0b53791da6b09626f5c074e1f421758e8f0b81bc110a0a895e224fc7bcbf")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-pandas@1.3:", type=("build", "run"))
    depends_on("py-numpy@1.21.2:1", type=("build", "run"))
    depends_on("py-matplotlib@3.8:3.8", type=("build", "run"))
    depends_on("py-seaborn@0.12:", type=("build", "run"))
    depends_on("py-scipy@1.12:", type=("build", "run"))
    depends_on("py-pysam@0.22.1", type=("build", "run"))
    depends_on("py-biopython@1.79:", type=("build", "run"))
    depends_on("py-adjusttext@0.7.3:0.8", type=("build", "run"))
    depends_on("py-liftover@1.1.13:1.3.1", type=("build", "run"))
    depends_on("py-scikit-allel@1.3.5:", type=("build", "run"))
    depends_on("py-pyensembl@2.2.3", type=("build", "run"))
    depends_on("py-gtfparse@1.3.0", type=("build", "run"))
    depends_on("py-h5py@3.10:", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-polars@1.27:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import gwaslab")
