# Copyright 2013-2023 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyPdmBackend(PythonPackage):
    """PDM's build backend that implements the latest packaging standards."""

    homepage = "https://backend.pdm-project.org/"
    pypi = "pdm_backend/pdm_backend-2.4.6.tar.gz"

    maintainers("softpack-bot")
    license("MIT")
    import_modules = ["pdm.backend"]

    version("2.4.6", sha256="5dd9cd581a4f18d57ff506a5b3aad7c8df31e5949b6fd854bbc34c38107e4532")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-importlib-metadata@3.6:", type=("build", "run"), when="^python@:3.9")

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
            python("-c", "import pdm.backend", env=env)
