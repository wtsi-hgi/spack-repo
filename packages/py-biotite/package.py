# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBiotite(PythonPackage):
    """A comprehensive library for computational molecular biology."""

    homepage = "https://www.biotite-python.org"
    pypi = "biotite/biotite-1.5.0.tar.gz"

    version(
        "1.5.0",
        sha256="1e1ac1d4aae111fef6a7b716c61730d50ed72df0d7cfd3523d264703dfedb5b8",
        expand=False,
        url="https://files.pythonhosted.org/packages/97/d4/be4a00d5f78002ab6d210bbacba4a76d8e2c1ec7fcbd3eb7325e7507d370/biotite-1.5.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl",
    )

    # Python requirement from PyPI metadata
    depends_on("python@3.11:", type=("build", "run"))

    # Runtime requirements from PyPI requires_dist
    depends_on("py-biotraj@1:1", type=("build", "run"))
    depends_on("py-msgpack@0.5.6:", type=("build", "run"))
    depends_on("py-networkx@2.0:", type=("build", "run"))
    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-packaging@24.0:", type=("build", "run"))
    depends_on("py-requests@2.12:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            # Library package; validate by import
            python("-c", "import biotite; print(biotite.__version__)")
