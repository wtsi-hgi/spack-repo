# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBidict(PythonPackage):
    """The bidirectional mapping library for Python."""

    homepage = "https://github.com/jab/bidict"
    pypi = "bidict/bidict-0.23.1.tar.gz"

    license("UNKNOWN")

    version("0.23.1", sha256="03069d763bc387bbd20e7d49914e75fc4132a41937fa3405417e1a5a2d006d71")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import bidict")
