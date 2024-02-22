# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLimixPlot(PythonPackage):
    """Plotting library for genetics."""

    homepage = "https://github.com/limix/limix-plot"
    pypi = "limix-plot/limix-plot-0.1.2.tar.gz"

    version("0.1.2", sha256="c6899bfd2e7ff1e75b0b0570fab75ec252239ceb617c2f8c2f06790f148bce43")

    depends_on("py-adjusttext@0.7.3:", type=("build", "run"))
    depends_on("py-matplotlib@3.0.3:", type=("build", "run"))
    depends_on("py-numpy@1.16.2:", type=("build", "run"))
    depends_on("py-pandas@0.24.2:", type=("build", "run"))
    depends_on("py-pillow@6.0.0:", type=("build", "run"))
    depends_on("py-pytest@4.4.1:", type=("build", "run"))
    depends_on("py-scikit-learn@0.20.3:", type=("build", "run"))
    depends_on("py-scipy@1.2.1:", type=("build", "run"))
    depends_on("py-xarray@0.12.1:", type=("build", "run"))
