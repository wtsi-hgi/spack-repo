# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpentelemetrySdk(PythonPackage):
    """OpenTelemetry Python SDK."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_sdk/opentelemetry_sdk-1.21.0.tar.gz"

    version("1.21.0", sha256="3ec8cd3020328d6bc5c9991ccaf9ae820ccb6395a5648d9a95d3ec88275b8879")

    depends_on("py-opentelemetry-api", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
