# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyInterlap(PythonPackage):
    """InterLap: simple, fast interval overlap testing."""

    homepage = "http://brentp.github.io/interlap/"
    pypi = "interlap/interlap-0.2.7.tar.gz"

    version("0.2.7", sha256="31e4f30c54b067c4939049f5d8131ae5e2fa682ec71aa56f89c0e5b900806ec9")

    depends_on("py-setuptools", type="build")
