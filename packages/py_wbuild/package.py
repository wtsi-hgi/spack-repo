# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWbuild(PythonPackage):
    """wBuild is all about making your day easier resolving, updating and cascading various dependencies, pipeline rules and code structs. The program lets you specify all the needed information in a YAML header right in your R code and let the automated :code:Snakemake processes do the rest!"""

    homepage = "https://github.com/gagneurlab/wBuild"
    pypi = "wbuild/wbuild-1.8.0.tar.gz"

    version("1.8.0", sha256="3088d3fcbc71106464f20e3546a73df400dc03d17f11e70bdb15d35d7e6c5a7e")

    depends_on("bumpversion@0.5.3:", type=("build", "run"))
    depends_on("py-watchdog@0.8.3:", type=("build", "run"))
    depends_on("py-flake8@2.6.0:", type=("build", "run"))
    depends_on("py-sphinx@1.4.8:", type=("build", "run"))
    depends_on("py-cryptography@1.7:", type=("build", "run"))
    depends_on("py-pyyaml@4.2:", type=("build", "run"))
    depends_on("py-sphinx-rtd-theme@0.3.1:", type=("build", "run"))
