# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStrictyaml(PythonPackage):
    """StrictYAML is a type-safe YAML parser that parses and validates a restricted subset of the YAML specification."""

    homepage = "https://hitchdev.com/strictyaml/"
    pypi = "strictyaml/strictyaml-1.7.3.tar.gz"

    version("1.7.3", sha256="22f854a5fcab42b5ddba8030a0e4be51ca89af0267961c8d6cfa86395586c407")

    depends_on("py-python-dateutil@2.6.0:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
