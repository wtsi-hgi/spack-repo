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

    depends_on("py-setuptools", type="build")

    depends_on("py-marshmallow@3.11:", type=("build", "run"))
