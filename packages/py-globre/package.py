# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyGlobre(PythonPackage):
    """Converts a glob-matching pattern to a regular expression, using Apache Cocoon style rules (with some extensions)."""

    homepage = "https://www.example.com"
    pypi = "globre/globre-0.1.5.tar.gz"

    version("0.1.5", sha256="ee214204f237e9114b8f61eeb61c2abd1e665ca3b59e5a6a0b070971c0bb12e2")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import globre")
