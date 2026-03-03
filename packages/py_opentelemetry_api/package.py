# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpentelemetryApi(PythonPackage):
    """OpenTelemetry Python API."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api"
    pypi = "opentelemetry_api/opentelemetry_api-1.21.0.tar.gz"

    version("1.21.0", sha256="d6185fd5043e000075d921822fd2d26b953eba8ca21b1e2fa360dd46a7686316")

    depends_on("py-importlib-metadata@6.0:7.0", type=("build", "run"))
    depends_on("py-hatchling", type=("build", "run"))
