# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypogrify(PythonPackage):
    """Typogrify provides a set of custom filters that automatically apply various transformations to plain text in order to yield typographically-improved HTML. While often used in conjunction with Jinja and Django template systems, the filters can be used in any environment."""

    homepage = "https://www.example.com"
    pypi = "typogrify/typogrify-2.1.0.tar.gz"

    version("2.1.0", sha256="f0aa004e98032a6e6be4c9da65e7eb7150e36ca3bf508adbcda82b4d003e61ee")

    depends_on("py-hatchling", type=("build"))
    depends_on("py-smartypants", type=("build", "run"))
