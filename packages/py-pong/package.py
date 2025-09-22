# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPong(PythonPackage):
    """Ultra-fast analysis and interactive visualization of population
    structure plots from Structure/Admixture data."""

    homepage = "https://github.com/ramachandran-lab/pong"
    pypi = "pong/pong-1.5.tar.gz"

    license("GPL-3.0-only")

    version("1.5", sha256="766e152f2b5d3bdcc506d92993ca8528ae77d8ee79b581d32c1eb48a073f6736")

    # Build dependencies
    depends_on("py-setuptools", type="build")

    # Runtime dependencies
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-numpy@1.19:1", type=("build", "run"))
    depends_on("py-tornado@6.1:6", type=("build", "run"))
    depends_on("py-munkres@1.1:1", type=("build", "run"))
    depends_on("py-networkx@2.5:2", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        # Prefer CLI check; fallback to Python import
        with working_dir("spack-test", create=True):
            pong_cmd = which("pong")
            if pong_cmd:
                pong_cmd("-h")
            else:
                python = which("python")
                python("-c", "import pong")

