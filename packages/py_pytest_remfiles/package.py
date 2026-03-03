# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestRemfiles(PythonPackage):
    """Pytest plugin to create a temporary directory with remote files."""

    homepage = "https://github.com/horta/pytest-remfiles"
    pypi = "pytest-remfiles/pytest-remfiles-0.0.2.tar.gz"

    version("0.0.2", sha256="da9b47bfa1565abf5dffa07ef608e4d78570466a2b85e56ed76920cf66285b6e")

    depends_on("py-pytest-runner@5.1:", type=("build", "run"))
    depends_on("py-pytest@5.0.0:", type=("build", "run"))
