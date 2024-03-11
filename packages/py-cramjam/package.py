# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from os import remove

class PyCramjam(PythonPackage):
    """A collection of compression algorithms, all in one place thru a common (as possible) API."""

    homepage = "https://github.com/milesgranger/cramjam"
    pypi = "cramjam/cramjam-2.8.2.tar.gz"

    version("2.8.2", sha256="ec9c8997edef2d74d9190be8195eaf983c705066f4c6ea1d4a96a807b54b8a91")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-maturin", type=("build", "run"))
    depends_on("py-black@22.3.0:", type=("build", "run"))

    def patch(self):
        remove("cramjam-python/Cargo.lock")
