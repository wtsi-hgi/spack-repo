# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAsyncioAtexit(PythonPackage):
    """Async-aware exit hooks similar to :mod:`atexit`."""

    homepage = "https://github.com/minrk/asyncio-atexit"
    pypi = "asyncio-atexit/asyncio-atexit-1.0.1.tar.gz"

    license("MIT")

    version("1.0.1", sha256="1d0c71544b8ee2c484d322844ee72c0875dde6f250c0ed5b6993592ab9f7d436")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import asyncio_atexit")
