# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEnrich2(PythonPackage):
    """Enrich2 is a general software tool for processing, analyzing, and visualizing data from deep mutational scanning experiments."""

    homepage = "https://github.com/FowlerLab/Enrich2"
    git = "https://github.com/FowlerLab/Enrich2"

    version("1.3.1", tag="v1.3.1")

    depends_on("python@2.7.18", type=("build", "run"))

    depends_on("py-numpy@1.10.4:1.15.0", type=("build", "run"))
    depends_on("py-scipy@0.16.0:1.2.1", type=("build", "run"))
    depends_on("py-pandas@0.18.0:0.25.0", type=("build", "run"))
    depends_on("py-tables@3.2.0:3.6.1", type=("build", "run"))
    depends_on("py-statsmodels@0.6.1:0.10.1", type=("build", "run"))
    depends_on("py-matplotlib@1.4.3:2.2.2", type=("build", "run"))

