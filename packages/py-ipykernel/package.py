# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpykernel(PythonPackage):
    """This package provides the IPython kernel for Jupyter."""

    homepage = "https://github.com/ipython/ipykernel"
    pypi = "ipykernel/ipykernel-6.27.1.tar.gz"

    version("6.27.1", sha256="7d5d594b6690654b4d299edba5e872dc17bb7396a8d0609c97cb7b8a1c605de6")
    version("6.15.3", sha256="b81d57b0e171670844bf29cdc11562b1010d3da87115c4513e0ee660a8368765")

    depends_on("py-debugpy@1.6.5:", type=("build", "run"))
    depends_on("py-ipython@7.23.1:", type=("build", "run"))
    depends_on("py-comm@0.1.1:", type=("build", "run"))
    depends_on("py-traitlets@5.4.0:", type=("build", "run"))
    depends_on("py-jupyter-client@6.1.12:", type=("build", "run"))
    depends_on("py-jupyter-core@4.12:", type=("build", "run"))
    depends_on("py-nest-asyncio", type=("build", "run"))
    depends_on("py-tornado@6.1:", type=("build", "run"))
    depends_on("py-matplotlib-inline@0.1:", type=("build", "run"))
    depends_on("py-pyzmq@20:", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-hatchling", type=("build", "run"))
