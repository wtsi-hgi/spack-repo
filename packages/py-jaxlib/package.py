# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJaxlib(PythonPackage):
    """XLA library for JAX (binary wheels).

    This recipe installs prebuilt manylinux wheels from PyPI for CPU.
    """

    homepage = "https://github.com/jax-ml/jax"
    # Use explicit wheel URLs per-version; do not rely on sdist

    # Provide the CPU wheel matching Python 3.10 manylinux2014 x86_64
    version(
        "0.5.1",
        sha256="80c0ed5446644b383caa3e617540803bb0ef36e5609cd7756d4d2913a8de512e",
        expand=False,
        url="https://files.pythonhosted.org/packages/71/19/d9934cefe3c3153e93e1285b761a1f75fd482501c73bd0d1b77a4c50c792/jaxlib-0.5.1-cp311-cp311-manylinux2014_x86_64.whl",
    )

    # Force pip-based installation of the wheel
    build_system("python_pip")

    # Requirements from PyPI metadata
    depends_on("python@3.11:3.11", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-scipy@1.11.1:", type=("build", "run"))
    depends_on("py-ml-dtypes@0.2.0:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import jaxlib")
