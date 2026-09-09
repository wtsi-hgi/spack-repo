# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyArgparse(PythonPackage):
    """Backport of Python's built-in argparse module for older interpreters."""

    homepage = "https://github.com/ThomasWaldmann/argparse/"
    pypi = "argparse/argparse-1.4.0.tar.gz"

    license("PSF-2.0")

    version("1.4.0", sha256="62b089a55be1d8949cd2bc7e0df0bddb9e028faefc8c32038cc84862aefdd6e4")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import argparse")
