# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMemoizedProperty(PythonPackage):
    """A simple Python decorator for defining properties that only run their fget function once"""

    homepage = "https://github.com/estebistec/python-memoized-property"
    pypi = "memoized-property/memoized-property-1.0.3.tar.gz"

    version("1.0.0", sha256="6c810a692c80d02fbb7bb4e3c3c6ee2d74b0ae8c8f12ac55f5556a12e9607695")
    version("1.0.1", sha256="15b7b19d56dad8bbcaab3935c8880d5f3951a65714114384eeceb7262e91d23f")
    version("1.0.2", sha256="af37ebec7cbca7654e2036ed6913a4b74a4ea9eee350cea8f5916f0b4ded2827")
    version("1.0.3", sha256="4be4d0209944b9b9b678dae9d7e312249fe2e6fb8bdc9bdaa1da4de324f0fcf5")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import memoized_property")
