# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpentelemetryInstrumentation(PythonPackage):
    """This package provides a couple of commands that help automatically instruments a program:"""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-instrumentation"
    pypi = "opentelemetry_instrumentation/opentelemetry_instrumentation-0.42b0.tar.gz"

    version("0.42b0", sha256="6a653a1fed0f76eea32885321d77c750483e987eeefa4cbf219fc83559543198")

    depends_on("py-opentelemetry-api@1.4:", type=("build", "run"))
    depends_on("py-wrapt@1.0.0:2.0.0", type=("build", "run"))
