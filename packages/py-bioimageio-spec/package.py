# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBioimageioSpec(PythonPackage):
    """Contains specifications defined by the BioImage.IO community."""

    homepage = "https://github.com/bioimage-io/spec-bioimage-io"
    pypi = "bioimageio.spec/bioimageio.spec-0.4.9.post5.tar.gz"

    version("0.4.9.post5", sha256="1b8e20be79a0f7e78c8dc1a7a2984646d9bcaeb811386a45de0806fc7757cc46")

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

    depends_on("py-marshmallow-jsonschema", type=("build", "run"))
    depends_on("py-marshmallow-union", type=("build", "run"))
    depends_on("py-marshmallow@3.6.0:4.0", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-packaging@17.0:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-ruamel-yaml", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-typer", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
