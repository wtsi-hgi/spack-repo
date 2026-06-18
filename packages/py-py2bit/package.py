# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPy2bit(PythonPackage):
    """Bindings for reading UCSC 2bit genome files via lib2bit."""

    pypi = "py2bit/py2bit-1.0.1.tar.gz"

    license("MIT")

    version("1.0.1", sha256="4972f85eb3844cdfba43eb54ab3c8349a0536e03dfd7db07ca8d3447285ad20c")
    version("0.3.3", sha256="264f5bfc39d729f1acad54c760ac04fa8a20d4184f4b505d9c333d2e03253770")
    version("0.2.1", sha256="34f7ac22be0eb4b5493063826bcc2016a78eb216bb7130890b50f3572926aeb1")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import py2bit")
