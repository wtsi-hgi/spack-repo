# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetrySemanticConventions(PythonPackage):
    """This library contains generated code for the semantic conventions defined by the OpenTelemetry specification."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-semantic-conventions"
    pypi = "opentelemetry_semantic_conventions/opentelemetry_semantic_conventions-0.42b0.tar.gz"

    version("0.42b0", sha256="44ae67a0a3252a05072877857e5cc1242c98d4cf12870159f1a94bec800d38ec")

    depends_on("py-hatchling", type=("build", "run"))
