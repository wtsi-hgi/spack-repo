# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyScienceplots(PythonPackage):
    """Format Matplotlib for scientific plotting"""
    homepage = "https://github.com/garrettj403/SciencePlots/wiki"
    pypi = "SciencePlots/scienceplots-2.2.2-py3-none-any.whl"

    license("MIT")

    version(
        "2.2.2",
        sha256="f63d04e6ec11fe2036ec120feb6c2f1d84b7c38e96cc7edcde7208064653af98",
        expand=False,
        url="https://files.pythonhosted.org/packages/5d/ff/6469a5cabf230ebc94f927246874136098dde1aacc9328bc40dceb24ba13/scienceplots-2.2.2-py3-none-any.whl",
    )

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))

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

            python("-c", "import scienceplots", env=env)
