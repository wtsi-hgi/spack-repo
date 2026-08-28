# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PySysmexcbctools(PythonPackage):
    """Toolkit for processing and analysing Sysmex CBC data."""

    homepage = "https://github.com/TheSeparatrix/SysmexCBCTools"
    git = "https://github.com/TheSeparatrix/SysmexCBCTools.git"

    license("MIT")

    version("20260826", commit="1b82fbd70629fbf51532126f198222e6671f10a6")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-numpy@1.24:", type=("build", "run"))
    depends_on("py-pandas@2.0:", type=("build", "run"))
    depends_on("py-pyyaml@5.4.0:", type=("build", "run"))
    depends_on("py-tqdm@4.60.0:", type=("build", "run"))
    depends_on("py-psutil@5.8.0:", type=("build", "run"))
    depends_on("py-pyarrow@3.0.0:", type=("build", "run"))
    depends_on("py-duckdb@0.9.0:", type=("build", "run"))
    depends_on("py-scipy@1.5.0:", type=("build", "run"))
    depends_on("py-scikit-learn@0.24.0:", type=("build", "run"))
    depends_on("py-matplotlib@3.3.0:", type=("build", "run"))
    depends_on("py-joblib@1.0.0:", type=("build", "run"))
    depends_on("py-pot@0.8.0:", type=("build", "run"))
    depends_on("py-pygam@0.8.0:", type=("build", "run"))
    depends_on("py-torch@1.8.0:", type=("build", "run"))
    depends_on("py-jupyter@1.0.0:", type=("build", "run"))
    depends_on("py-seaborn@0.11.0:", type=("build", "run"))
    depends_on("py-ipywidgets@7.0:", type=("build", "run"))
    depends_on("py-scienceplots@2.0.0:", type=("build", "run"))
    depends_on("py-phate@1.0.0:", type=("build", "run"))

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

            python(
                "-c",
                "import sysmexcbctools; "
                "assert sysmexcbctools.XNSampleProcessor is not None",
                env=env,
            )
