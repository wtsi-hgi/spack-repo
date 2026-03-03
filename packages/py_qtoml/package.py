# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQtoml(PythonPackage):
    """qtoml is another Python TOML encoder/decoder. I wrote it because I found uiri/toml too unstable, and PyTOML too slow."""

    homepage = "https://github.com/alethiophile/qtoml"
    pypi = "qtoml/qtoml-0.3.1.tar.gz"

    version("0.3.1", sha256="7f2d0c2c39659d2a408ae93d02a068e0d22eb67e16e474239f7735ff1094b1ba")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-click@7.0:9.0", type=("build", "run"))
    depends_on("py-attrs@19.3.0:22.0", type=("build", "run"))
    depends_on("py-python-dateutil@2.7:", type=("build", "run"))
    depends_on("py-pytz@2018.9:", type=("build", "run"))
    depends_on("py-click@7.0:9.0", type=("build", "run"))
    depends_on("py-hypothesis@5.1.4:", type=("build", "run"))
    depends_on("py-pytest@5.3.2:", type=("build", "run"))
    depends_on("py-mypy@0.761:", type=("build", "run"))
    depends_on("py-poetry@0.12:", type=("build", "run"))
