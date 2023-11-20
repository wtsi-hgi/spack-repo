# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLiknorm(PythonPackage):
    """Liknorm Python wrapper."""

    homepage = "https://github.com/limix/liknorm-py"
    pypi = "liknorm/liknorm-1.2.10.tar.gz"

    version("1.2.10", sha256="ce1fec274584e52ae8879aec9fb9849e9081d0c99485a45b87266ee1f6c803d7")

    depends_on("python@3.8:3.12", type=("build", "run"))
    depends_on("py-cffi", type=("build", "run"))
    depends_on("py-pytest ", type=("build", "run"))
    depends_on("py-urllib3@1.26", type=("build", "run"))
    depends_on("py-black", type=("build", "run"))
    depends_on("py-isort", type=("build", "run"))
    depends_on("py-pyright", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-poetry", type=("build", "run"))
    depends_on("py-cmake", type="build")
