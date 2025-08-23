# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPanel(PythonPackage):
    """A high level app and dashboarding solution for Python."""

    homepage = "http://panel.holoviz.org/"
    pypi = "panel/panel-0.14.4.tar.gz"

    version("0.14.4", sha256="b853d2f53d7738ec6372525360c5bf9427a71ed990685ccac703bc9b442e9951")

    depends_on("py-param@1.12:", type=("build", "run"))
    depends_on("py-pyct@0.4.4:", type=("build", "run"))
    depends_on("py-setuptools@42:", type=("build", "run"))
    depends_on("py-bokeh@2.4.3:2.4", type=("build", "run"))
    depends_on("py-pyviz-comms@0.7.4:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-bleach", type=("build", "run"))
    depends_on("py-packaging", type="build")
    # tqdm 4.66.1 is broken under our Python 3.9 toolchain (installs only dist-info)
    # Constrain to <=4.65 to ensure module files are present during build
    depends_on("py-tqdm@4.48:4.65", type=("build", "run"))
    depends_on("py-markdown", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("node-js@14:", type=("build", "run"))
