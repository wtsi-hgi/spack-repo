# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTinytimer(PythonPackage):
    """Minimal wall-clock timer helper."""

    homepage = "https://github.com/openvax/tinytimer"
    pypi = "tinytimer/tinytimer-0.0.0.tar.gz"

    version("0.0.0", sha256="6ad13c8f01ab6094e58081a5367ffc4c5831f2d6b29034d2434d8ae106308fa5")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import tinytimer")
