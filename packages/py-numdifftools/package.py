# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyNumdifftools(PythonPackage):
    """Solve automatic numerical differentiation problems in one or more variables."""

    homepage = "https://github.com/pbrod/numdifftools"
    pypi = "numdifftools/numdifftools-0.9.41.tar.gz"

    maintainers("softpack-bot")
    license("BSD-3-Clause")
    import_modules = ["numdifftools"]

    version("0.9.42", sha256="866675171f293c4bf2f1e1c5bf9b88a07d5396903e3b3e7fcc3879e2a01cfbc1")
    version("0.9.41", sha256="4ef705cd3c06211b3a4e9fd05ad622be916dcfda40732f0128805a2c4be389b4")

    depends_on("python@3.10:", type=("build", "run"), when="@0.9.42:")
    depends_on("python@3.7:", type=("build", "run"), when="@:0.9.41")

    depends_on("py-pdm-backend", type="build", when="@0.9.42:")
    depends_on("py-setuptools", type="build", when="@:0.9.41")

    depends_on("py-numpy@1.21.2:", type=("build", "run"), when="@0.9.42:")
    depends_on("py-numpy@1.9:", type=("build", "run"), when="@:0.9.41")

    depends_on("py-scipy@1.7.3:", type=("build", "run"), when="@0.9.42:")
    depends_on("py-scipy@0.8:", type=("build", "run"), when="@:0.9.41")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            pyver = self.spec["python"].version.up_to(2)
            site_packages = join_path(self.prefix, f"lib/python{pyver}", "site-packages")
            env = os.environ.copy()
            env["PYTHONPATH"] = (
                f"{site_packages}{os.pathsep}{env['PYTHONPATH']}"
                if env.get("PYTHONPATH")
                else site_packages
            )
            python("-c", "import numdifftools", env=env)
