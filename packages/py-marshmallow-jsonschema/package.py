# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarshmallowJsonschema(PythonPackage):
    """marshmallow-jsonschema translates marshmallow schemas into JSON Schema Draft v7 compliant jsonschema."""

    homepage = "https://github.com/fuhrysteve/marshmallow-jsonschema"
    pypi = "marshmallow-jsonschema/marshmallow-jsonschema-0.13.0.tar.gz"

    version("0.13.0", sha256="f8ce19cfc0edd909e81f141d7420c33544b849bc5ebbfae8f6a3deea5a3b1f47")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    depends_on("py-marshmallow@3.11:", type=("build", "run"))
