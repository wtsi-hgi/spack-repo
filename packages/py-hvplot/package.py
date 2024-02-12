# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHvplot(PythonPackage):
    """hvPlot makes data analysis and visualization simple."""

    homepage = "https://hvplot.holoviz.org/"
    pypi = "hvplot/hvplot-0.9.2.tar.gz"

    version("0.9.2", sha256="9a8c9e9249139aaa3dee5f1cea0f93cf36374d179e986705fcddc2b92c470793")

    depends_on("py-param@1.7.0:", type=("build", "run"))
    depends_on("py-pyct@0.4.4:", type=("build", "run"))
