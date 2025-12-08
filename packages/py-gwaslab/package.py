# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGwaslab(PythonPackage):
    """Handy utilities for processing and visualizing GWAS summary statistics."""

    homepage = "https://cloufield.github.io/gwaslab/"
    pypi = "gwaslab/gwaslab-3.6.13.tar.gz"

    version("3.6.13", sha256="82ba0b53791da6b09626f5c074e1f421758e8f0b81bc110a0a895e224fc7bcbf")
    version("3.6.9", sha256="9d864f7d30217c643d577435c4d7879ce51ce9aad96bba70fa97f4a46e66d1fe")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:3.12", type=("build", "run"))

    depends_on("py-pandas@1.3:", type=("build", "run"))
    conflicts("^py-pandas@1.5.0:1.5")

    depends_on("py-numpy@1.21.2:", type=("build", "run"))
    conflicts("^py-numpy@2:")

    depends_on("py-matplotlib@3.8:", type=("build", "run"))
    conflicts("^py-matplotlib@3.9:")

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
            python = self.spec["python"].command
            python("-c", "import gwaslab")
