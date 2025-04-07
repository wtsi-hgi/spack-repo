# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIpympl(PythonPackage):
    """Matplotlib Jupyter Extension."""

    homepage = "https://github.com/matplotlib/ipympl"
    pypi = "ipympl/ipympl-0.8.8.tar.gz"
    maintainers("haralmha")

    version("0.9.4", sha256="cfb53c5b4fcbcee6d18f095eecfc6c6c474303d5b744e72cc66e7a2804708907")
    version("0.8.8", sha256="5bf5d780b07fafe7924922ac6b2f3abd22721f341e5e196b3b82737dfbd0e1c9", deprecated=True)

    depends_on("py-setuptools@40.8:", type="build")
    depends_on("py-ipython@:8", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-ipython-genutils", type=("build", "run"))
    depends_on("pil", type=("build", "run"))
    depends_on("py-traitlets@:5", type=("build", "run"))
    depends_on("py-ipywidgets@7.6:7", type=("build", "run"), when="@:0.8")
    depends_on("py-ipywidgets@7.6:8", type=("build", "run"), when="@0.9:")
    depends_on("py-matplotlib@2:3", type=("build", "run"), when="@:0.8")
    depends_on("py-matplotlib@3.4:3", type=("build", "run"), when="@0.9:")
    depends_on("py-jupyter-core", type=("build", "run"))
    depends_on("py-jupyter-packaging@0.7", type="build", when="@:0.8")
    depends_on("py-jupyterlab@3", type="build", when="@:0.8")
    depends_on("py-jupyterlab@4", type="build", when="@0.9:")
    depends_on("yarn@1", type="build", when="@:0.8")
    depends_on("node-js", type="build")
    depends_on("py-hatchling", type="build", when="@0.9:")
    depends_on("py-hatch-nodejs-version@0.3.2:", type="build", when="@0.9:")
