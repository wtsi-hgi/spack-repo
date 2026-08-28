# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyPhate(PythonPackage):
    """PHATE"""

    homepage = "https://github.com/KrishnaswamyLab/PHATE"
    pypi = "phate/phate-2.0.0-py3-none-any.whl"

    license("GPL-2.0-only")

    version(
        "2.0.0",
        sha256="d0ca74b188d5397be78a5be11322ca0841738b73f3e27986a6f8eb7e799d2d73",
        expand=False,
        url="https://files.pythonhosted.org/packages/32/7f/ab3e73eac07a3d7f0dae6f81028744f2702512cb5a1376870e6de95b7450/phate-2.0.0-py3-none-any.whl",
    )

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.20.0:", type=("build", "run"))
    depends_on("py-scipy@1.7.0:", type=("build", "run"))
    depends_on("py-scikit-learn@1.5.0:", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
    depends_on("py-tasklogger@1.2:", type=("build", "run"))
    depends_on("py-graphtools@2.1.0:", type=("build", "run"))
    depends_on("py-deprecated", type=("build", "run"))
    depends_on("py-matplotlib@3.0:", type=("build", "run"))

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

            lib_dirs = []
            for dep in self.spec.traverse(root=False):
                for subdir in ("lib", "lib64"):
                    candidate = join_path(dep.prefix, subdir)
                    if os.path.isdir(candidate):
                        lib_dirs.append(candidate)
            if lib_dirs:
                env["LD_LIBRARY_PATH"] = (
                    f"{os.pathsep.join(lib_dirs)}{os.pathsep}{env['LD_LIBRARY_PATH']}"
                    if env.get("LD_LIBRARY_PATH")
                    else os.pathsep.join(lib_dirs)
                )

            python("-c", "import phate", env=env)
