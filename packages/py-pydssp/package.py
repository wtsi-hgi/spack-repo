# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPydssp(PythonPackage):
    """Simplified DSSP secondary-structure prediction implemented for PyTorch and NumPy."""

    homepage = "https://github.com/ShintaroMinami/PyDSSP"
    pypi = "pydssp/pydssp-0.9.1-py3-none-any.whl"

    version(
        "0.9.1",
        sha256="74fb8129c07c1625bb687b80f7e94ae7ebf1277725258d7fc75fc1f3d12a67dc",
        expand=False,
        url="https://files.pythonhosted.org/packages/00/78/9cbcc1c073b9d4918e925af1a059762265dc65004e020511b2a06fbfd020/pydssp-0.9.1-py3-none-any.whl",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-einops", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))

    def install(self, spec, prefix):
        from spack.build_systems.python import PythonPipBuilder

        pip(*PythonPipBuilder.std_args(self), f"--prefix={prefix}", self.stage.archive_file)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import pydssp")
