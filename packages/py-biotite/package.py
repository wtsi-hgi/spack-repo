# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBiotite(PythonPackage):
    """A comprehensive library for computational molecular biology."""

    homepage = "https://www.biotite-python.org"
    pypi = "biotite/biotite-1.5.0.tar.gz"

    # Prefer wheel to avoid hatchling/hatch-vcs build-time plugins
    version(
        "1.5.0-py311",
        sha256="b57ea328f87c8b1109d182c34baab3db0f88e975b66d9e4d9b711af6acb1f483",
        expand=False,
        url="https://files.pythonhosted.org/packages/75/de/e8d669683bd3dd1adc872e4d013c8c92e25f6d33728685a9b4769d0b4bad/biotite-1.5.0-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl",
    )

    # Build dependency
    depends_on("py-hatchling", type=("build"))
    depends_on("py-hatch-vcs", type=("build"))

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
            # Library package; validate by import
            python("-c", "import biotite; print(biotite.__version__)")
