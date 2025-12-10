# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTypechecks(PythonPackage):
    """Utilities for validating arguments at runtime."""

    homepage = "https://github.com/openvax/typechecks"
    pypi = "typechecks/typechecks-0.1.0.tar.gz"

    version("0.1.0", sha256="7d801a6018f60d2a10aa3debc3af65f590c96c455de67159f39b9b183107c83b")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import typechecks")
