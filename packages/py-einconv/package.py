# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyEinconv(PythonPackage):
    """Convolutions as tensor contractions (einsums) for PyTorch."""

    homepage = "https://github.com/f-dangel/einconv"
    pypi = "einconv/einconv-0.1.0.tar.gz"

    maintainers("softpack-bot")
    license("MIT")
    import_modules = ["einconv"]

    version("0.1.0", sha256="6b103881b1268e43d581f285da4fa72b073c95f31b92575133bafed9929b6d98")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-torch", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            pyver = self.spec["python"].version.up_to(2)
            site_packages = join_path(self.prefix, f"lib/python{pyver}", "site-packages")
            env = os.environ.copy()
            pythonpaths = [site_packages]
            for dependency in self.spec.traverse(order="post", deptype=("build", "run")):
                candidate = join_path(dependency.prefix, f"lib/python{pyver}", "site-packages")
                if os.path.isdir(candidate) and candidate not in pythonpaths:
                    pythonpaths.append(candidate)
            if env.get("PYTHONPATH"):
                pythonpaths.append(env["PYTHONPATH"])
            env["PYTHONPATH"] = os.pathsep.join(pythonpaths)
            python("-c", "import einconv", env=env)
