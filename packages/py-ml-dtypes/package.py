# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMlDtypes(PythonPackage):
    """NumPy dtype extensions used in ML libraries (binary wheels)."""

    homepage = "https://github.com/jax-ml/ml_dtypes"

    version(
        "0.3.1",
        sha256="42a8980afd8b7c8e270e8b5c260237286b5b26acd276fcb758d13cd7cb567e99",
        expand=False,
        url="https://files.pythonhosted.org/packages/5f/b0/52580c12377c7f9a4319a80c85e235f4eeb7f8a09d362900dd3091b246ce/ml_dtypes-0.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
    )
    version(
        "0.5.1",
        sha256="c09526488c3a9e8b7a23a388d4974b670a9a3dd40c5c8a61db5593ce9b725bab",
        expand=False,
        url="https://files.pythonhosted.org/packages/cc/2a/5421fd3dbe6eef9b844cc9d05f568b9fb568503a2e51cb1eb4443d9fc56b/ml_dtypes-0.5.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
    )

    build_system("python_pip")

    depends_on("python@3.11:3.11", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "link", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import ml_dtypes")
