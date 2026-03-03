# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHic2cool(PythonPackage):
    """Converter between hic files (from juicer) and single-resolution or multi-resolution cool files (for cooler).  Both hic and cool files describe Hi-C contact matrices. Intended to be lightweight, this can be used as an imported package or a stand-alone Python tool for command line conversion."""

    homepage = "https://github.com/4dn-dcic/hic2cool/"
    url = "https://github.com/4dn-dcic/hic2cool/archive/refs/tags/1.0.1.tar.gz"

    version(
        "1.0.1",
        sha256="f1f1ffeeec8788819e6ae4b4d1236ba4349dceb98aa4a0b0b3068af30c2a6434",
    )
    depends_on("python@3.8:3.11", type=("build", "run"))
    depends_on("py-cooler", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-poetry-core", type="build")

    def patch(self):
        # need to patch the package for it to work with python 3.10
        filter_file('python = ">=3.8,<3.10"', 'python = ">=3.8,<3.11"', "pyproject.toml")

    @run_after("install")
    def run_test(self):
        # confirm the package works in python 3.10
        which("python")("test.py")


# {'cooler(>=0.7.2)': ['0.4.2'], 'h5py(>=2.8.0)': ['0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.7.0', '0.7.1', '0.7.2', '0.7.3', '0.8.0', '0.8.1', '0.8.2', '0.8.3'], 'numpy(>=1.10.1)': ['0.5.0', '0.5.1', '0.6.0', '0.6.1', '0.6.2', '0.8.2', '0.8.3'], 'cooler(>=0.8.2)': ['0.5.0', '0.5.1'], 'cooler(>=0.8.5)': ['0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.7.0', '0.7.1', '0.7.2', '0.7.3', '0.8.0', '0.8.1', '0.8.2', '0.8.3'], 'numpy(<=1.16.3,>=1.10.1)': ['0.6.3', '0.6.4', '0.6.5', '0.7.0', '0.7.1', '0.7.2', '0.7.3', '0.8.0', '0.8.1'], 'scipy(<=1.2.1)': ['0.6.4', '0.6.5', '0.7.0', '0.7.1', '0.7.2', '0.7.3', '0.8.0', '0.8.1'], 'pandas(<=0.24.2)': ['0.7.3', '0.8.0', '0.8.1'], 'scipy': ['0.8.2', '0.8.3'], 'pandas': ['0.8.2', '0.8.3'], 'cooler(==0.9.3)': ['1.0.0', '1.0.1'], 'h5py(>=2.5.0)': ['1.0.0', '1.0.1'], 'numpy(>=1.9)': ['1.0.0', '1.0.1'], 'pandas(>=1.0)': ['1.0.0', '1.0.1'], 'scipy(>=1.10.1)': ['1.0.0', '1.0.1']}
