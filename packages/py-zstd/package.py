# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyZstd(PythonPackage):
    """Python bindings for the Zstandard compression library."""

    homepage = "https://github.com/sergey-dryabzhinsky/python-zstd"
    pypi = "zstd/zstd-1.5.7.2.tar.gz"
    license("BSD-3-Clause")

    version("1.5.7.2", sha256="6d8684c69009be49e1b18ec251a5eb0d7e24f93624990a8a124a1da66a92fc8a")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import zstd; print(zstd.__name__)")
